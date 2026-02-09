import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def get_restaurant_data(restaurant_name, driver):
    url = f"https://fdc.nal.usda.gov/fdc-app.html#/?query={restaurant_name.replace(' ', '%20')}"
    driver.get(url)

    # Retry loading the page twice (it was sometimes not updating properly)
    for _ in range(2):
        driver.refresh()
        time.sleep(2)  # Waiting for page to reload

    # timer for content to appear to avoid crashing
    wait = WebDriverWait(driver, 4)
    try:
        span_element = wait.until(EC.element_to_be_clickable((By.ID, "srlegacy-food-tab-selector")))
        span_element.click()

        # Extract text content from the <span> elements (food names and links)
        data_elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//a[@name='food-search-result-description']")))
        restaurant_data = []
        for element in data_elements:
            food_item = element.text
            link = element.get_property("href")
            restaurant_data.append({"food_item": food_item, "link": link})
        return restaurant_data
    except TimeoutException: # timeout error case
        print(f"No data found for {restaurant_name} due to timeout.\n")
        return []
    except NoSuchElementException: # case for no links/data
        print(f"No links found for {restaurant_name}.\n")
        return []

def scrape_nutrient_info(url):
    driver = webdriver.Chrome() 
    driver.get(url)
    # different portions of nutrition data 
    nutrients = driver.find_elements(By.XPATH, "//span[@name='finalFoodNutrientName']")
    nutrient_vals = driver.find_elements(By.XPATH, "//span[@name='finalFoodNutrientValue']")
    nutrient_units = driver.find_elements(By.XPATH, "//span[@name='finalFoodNutrientStandardUnit']")

    nutrient_info = [] #scrape the nutrient name, value and units
    for n, v, u in zip(nutrients, nutrient_vals, nutrient_units):
        nutrient_info.append((n.text, v.text, u.text))

    driver.quit()

    return nutrient_info

def main():
    # same list of restaurants we used for other code
    restaurants = ["McDonald's", "Burger King", "KFC", "Pizza Hut", "In-N-Out Burger", "Subway", "Wendy's", "Taco Bell", "Starbucks", "Dunkin'"]
    driver = webdriver.Chrome()

    with open('restaurant_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # writing data into CSV
        fieldnames = ['Restaurant', 'Food', 'Nutrient', 'Value', 'Unit']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for restaurant in restaurants:
            print(f"Scraping data for {restaurant}:")
            restaurant_data = get_restaurant_data(restaurant, driver)
            
            #scraping food item names and links to use
            for item in restaurant_data:
                food_item = item["food_item"]
                link = item["link"]

                if not link:
                    print(f"No link available for {food_item}.")
                    continue

                # Scrape nutritional information for food
                nutrient_info = scrape_nutrient_info(link)

                # Write nutrient information/data to CSV, each portion as a different column
                for nutrient in nutrient_info:
                    writer.writerow({'Restaurant': restaurant, 'Food': food_item, 'Nutrient': nutrient[0], 'Value': nutrient[1], 'Unit': nutrient[2]})
                
                # Delay to avoid crashing
                time.sleep(2) 

    driver.quit()

if __name__ == "__main__":
    main()
