import os
import sqlite3
import requests
import csv
from dotenv import load_dotenv
from collections import Counter

load_dotenv()

# List of API keys, use one at a time, max 300 per day per key
API_KEYS = os.getenv('YELP_API_KEY')

# Yelp API call formula taken directly from Yelp, added in error catching 
def get_top_fast_food_chain(api_key, location):
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {
        'term': 'fast food',
        'location': location,
        'limit': 50
    }
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()['businesses']
    except requests.exceptions.RequestException as e: #error catching 
        print(f'Error for {location}: {e}')
        return None
    except KeyError:
        print(f'Key error for {location}')
        return None

def update_csv_with_yelp_data(csv_filename, locations):
    fast_food_chains = ["McDonald's", "Burger King", "KFC", "Pizza Hut", "In-N-Out Burger", "Subway", "Wendy's", "Taco Bell", "Starbucks", "Dunkin'"]

    if os.path.exists(csv_filename):
        with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
            existing_locations = set()
            reader = csv.DictReader(csvfile)
            for row in reader:
                existing_locations.add(row['Location'])

        locations_to_call = locations - existing_locations
    else:
        locations_to_call = locations

    with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Location', 'Name', 'Review Count', 'Marker']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not os.path.exists(csv_filename):
            writer.writeheader()

        api_calls = 0
        for location in locations_to_call:
            if api_calls >= 300:
                break
            keys_used = set()
            for api_key in API_KEYS:
                if api_key not in keys_used:
                    businesses = get_top_fast_food_chain(api_key, location)
                    api_calls += 1
                    keys_used.add(api_key)
                    if businesses:
                        # Filter out businesses not in the specified fast food chains
                        relevant_businesses = [business for business in businesses if business['name'] in fast_food_chains]
                        if relevant_businesses:
                            # Count occurrences of each fast food chain to choose most occurred 
                            chain_counts = Counter(business['name'] for business in relevant_businesses)
                            # Sort by count in descending order
                            sorted_chains = sorted(chain_counts.items(), key=lambda x: (-x[1], x[0]))
                            # most common chain based on count 
                            most_common_chain = sorted_chains[0][0]
                            # If there's a tie, the most prominent will be the one with the most reviews
                            if len(sorted_chains) > 1 and sorted_chains[0][1] == sorted_chains[1][1]:
                                review_counts = {business['name']: business['review_count'] for business in relevant_businesses}
                                most_common_chain = max(sorted_chains, key=lambda x: (x[1], -review_counts.get(x[0], 0)))[0]
                            review_count = max(business['review_count'] for business in relevant_businesses if business['name'] == most_common_chain)
                            writer.writerow({
                                'Location': location,
                                'Name': most_common_chain,
                                'Review Count': review_count,
                                'Marker': '✔', # marker to know that it has already been gotten from Yelp API
                            })
                            print(f"Fast food chain data saved for: {location}")
                        else:
                            # If no relevant fast food chains found, select None
                            writer.writerow({
                                'Location': location,
                                'Name': 'None',
                                'Review Count': 0,
                                'Marker': '✔',
                            })
                            print(f"No relevant fast food chains found for: {location}")
                        break
                    else:
                        print(f"No data for {location} from API key: {api_key}.")
                else:
                    continue
            else:
                continue

    print(f"Total API calls made: {api_calls}")
    print("CSV file update part 1 updated")

def main():
    try:
        conn = sqlite3.connect('powerlifting_data.db')
        cursor = conn.cursor()

        # Get locations from the database (already created db in powerlifting_and_locations_todb.py)
        cursor.execute("SELECT city || ', ' || state FROM locations")
        locations = set(row[0] for row in cursor.fetchall())

        # Update CSV with Yelp API called data
        update_csv_with_yelp_data('fast_food_chains.csv', locations)

        print("CSV file update part 2 updated")
    except sqlite3.Error as e:
        print(f'SQLite error: {e}')
    finally:
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == "__main__":
    main()
