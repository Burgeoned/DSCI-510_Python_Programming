# Strength & Sustenance: Mapping Fast Food Density vs. Powerlifting Performance 
## DSCI-510: Python Programming (Spring 2024)

University of Southern California | MS Applied Data Science

## Research Hypothesis
In the powerlifting community, the "dirty bulk" mentality suggests that high-calorie, processed foods are effective fuel for extreme strength gains.  This project investigates that narrative by joining athletic performance data with geospatial and nutritional insights to determine if the proximity of fast-food establishments correlates with higher Wilks Scores in competitive lifters.



## Data Architecture
The project utilizes a relational database structure with five integrated tables to link environmental factors to athletic outcomes:


**openpowerlifting:** Performance records for competitive athletes (Lifts, Sex, Age, Bodyweight).


**locations:** A central reference table used to join athletic meets with local business data by State and City.


**yelp_data:** High-visitation fast-food locations retrieved via the Yelp Fusion API.


**fast_food_reference:** A normalized table for mapping specific chains (e.g., McDonald's, In-N-Out) to unique IDs.


**restaurant_data:** Detailed macronutrient profiles (Protein, Fat, Carbohydrates) scraped from USDA FoodData Central.


## Technical Pipeline
The system is built as a multi-stage data engineering pipeline:


**Data Initialization (powerlifting_and_locations_todb.py):** Filters the OpenPowerlifting dataset for SBD (Squat, Bench, Deadlift) events and initializes the primary SQLite location and performance tables.


**Web Scraping (WebScrapeCSVScript.py):** A Selenium-based automation script that navigates the USDA FoodData Central portal to extract high-fidelity nutritional data for specific fast-food menus.


**Geospatial Harvesting (YelpAPIScript.py):** Utilizes the Yelp Fusion API to identify and map the density of fast-food chains surrounding historical powerlifting meet locations.


**Database Integration (Lee_Jack_proj2.py):** Reconciles the scraped CSVs and API outputs into a final SQLite database, building the relational links required for multi-factor analysis.


**Interactive Deployment (Final_Project_Streamlit.py):** A Streamlit application that provides real-time filtering (by gender, age, and equipment) and visualizes the correlation between average macronutrient density and total weight lifted.



## Tech Stack
**Language:** Python 3.x 

**Libraries:** Pandas (Data Cleaning/Analysis), NumPy, Requests (APIs), BeautifulSoup (Web Scraping), SQLite (Database Management). 

**Deployment:** Streamlit (Interactive Visualization & UI).



## Repository Structure
**Final_Project_Streamlit.py:** The core application for the interactive dashboard.


**WebScrapeCSVScript.py:** Selenium scraper for government nutritional data.


**YelpAPIScript.py:** Yelp Fusion API integration script.


**powerlifting_and_locations_todb.py:** Database initialization script.


**Lee_Jack_proj2.py:** Final data integration and SQL table building.

**requirements.txt:** Project dependencies for deployment.

## PM Note: The "Dirty Bulk" Insight
"This project was driven by a desire to validate 'gym talk' with objective data. By merging nutritional density from government sources with live Yelp location data, I was able to model how a lifter's immediate environment impacts their performance outcomes. It demonstrates my ability to take a niche behavioral hypothesis and build a technical pipeline to test it."
