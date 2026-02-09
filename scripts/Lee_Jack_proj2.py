import sqlite3
import csv

def create_fast_food_reference_table(conn, chains):
    try:
        # reference table to match fast food chain 
        conn.execute('''CREATE TABLE IF NOT EXISTS fast_food_reference (
                        id INTEGER PRIMARY KEY,
                        chain_name TEXT UNIQUE
                        )''')
        
        # fast food chains
        for chain in chains: 
            conn.execute("INSERT OR IGNORE INTO fast_food_reference (chain_name) VALUES (?)", (chain,))
        
        # set Others to ID 999
        conn.execute("INSERT OR IGNORE INTO fast_food_reference (id, chain_name) VALUES (?, ?)", (999, "Other"))
        
        conn.commit()
        print("Fast food reference table built")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

def insert_yelp_data(conn, csv_filename):
    try:
        # inserting yelp data from yelp api script produced csv
        with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                location = row['Location']
                name = row['Name']
                review_count = row['Review Count']
                # Get location ID to match location reference table 
                location_id = conn.execute("SELECT id FROM locations WHERE city || ', ' || state = ?", (location,)).fetchone()[0]
                # Get fast food chain ID to match fast food reference table
                chain_id_query = conn.execute("SELECT id FROM fast_food_reference WHERE chain_name = ?", (name,))
                chain_id_result = chain_id_query.fetchone()
                if chain_id_result is None:  # If no match found, set chain_id to "Other"
                    chain_id = conn.execute("SELECT id FROM fast_food_reference WHERE chain_name = ?", ("Other",)).fetchone()[0]
                else:
                    chain_id = chain_id_result[0]
                conn.execute("INSERT INTO yelp_data (location_id, name, review_count, fast_food_chain_id) VALUES (?, ?, ?, ?)",
                             (location_id, name, review_count, chain_id))
            conn.commit()
        print("Yelp data added")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")



def insert_restaurant_data(conn, csv_filename):
    try:
        with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                restaurant = row['Restaurant']  # fast food restaurant name
                food_item = row['Food']
                protein = row['Protein']
                fat = row['Fat']
                carbohydrates = row['Carbohydrates']
                
                # Get fast food chain ID from other table
                chain_id_query = conn.execute("SELECT id FROM fast_food_reference WHERE chain_name = ?", (restaurant,))
                chain_id_result = chain_id_query.fetchone()
                chain_id = chain_id_result[0] if chain_id_result else None  # id to None if there is no fast food chain found with it
                
                # Insert restaurant data into the database
                conn.execute("INSERT INTO restaurant_data (restaurant, fast_food_chain_id, food, Protein, Fat, Carbohydrates) VALUES (?, ?, ?, ?, ?, ?)",
                             (restaurant, chain_id, food_item, protein, fat, carbohydrates))
            
            conn.commit()
            print("Restaurant data added")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")


def main():
    try:
        conn = sqlite3.connect('powerlifting_data.db')

        # Create fast food reference table
        fast_food_chains = ["McDonald's", "Burger King", "KFC", "Pizza Hut", "In-N-Out Burger", "Subway", "Wendy's", "Taco Bell", "Starbucks", "Dunkin'"]
        create_fast_food_reference_table(conn, fast_food_chains)

        conn.execute('''CREATE TABLE IF NOT EXISTS yelp_data (
                        location_id INTEGER,
                        name TEXT,
                        review_count INTEGER,
                        fast_food_chain_id INTEGER,
                        FOREIGN KEY (location_id) REFERENCES locations(id),
                        FOREIGN KEY (fast_food_chain_id) REFERENCES fast_food_reference(id)
                        )''')

        conn.execute('''CREATE TABLE IF NOT EXISTS restaurant_data (
                    id INTEGER PRIMARY KEY,
                    restaurant TEXT,
                    food TEXT,
                    protein INTEGER,
                    fat INTEGER,
                    carbohydrates INTEGER,
                    fast_food_chain_id INTEGER,
                    FOREIGN KEY (fast_food_chain_id) REFERENCES fast_food_reference(id)
                )''')

        # Yelp CSV
        insert_yelp_data(conn, 'fast_food_chains.csv')

        # WebScraped CSV
        insert_restaurant_data(conn, 'restaurant_data.csv')

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    finally:
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == "__main__":
    main()
