# Strength & Sustenance: Mapping Fast Food Density vs. Powerlifting Performance 
## DSCI-510: Python Programming (Spring 2024)

University of Southern California | MS Applied Data Science

## Research Hypothesis
In the powerlifting community, the "dirty bulk" mentality suggests that high-calorie, processed foods are effective fuel for extreme strength gains.  This project investigates that narrative by joining athletic performance data with geospatial and nutritional insights to determine if the proximity of fast-food establishments correlates with higher Wilks Scores in competitive lifters.



## The Data Pipeline
This project integrates three distinct data sources to build a comprehensive view of the lifting environment: 


**Government Food Data (Scraped):** Nutritional profiles and caloric density metrics extracted from federal databases using BeautifulSoup. 


**Yelp Fusion API (Live Integration):** Geospatial coordinates and business metadata for fast-food establishments within a radius of competition venues. 


**Powerlifting Federation Data (CSV):** Historical performance metrics (lifts, body weight, and Wilks scores) for competitive athletes.



## Tech Stack
**Language:** Python 3.x 

**Libraries:** Pandas (Data Cleaning/Analysis), NumPy, Requests (APIs), BeautifulSoup (Web Scraping), SQLite (Database Management). 

**Deployment:** Streamlit (Interactive Visualization & UI).



## Repository Structure
**app.py:** The core Streamlit application script for the interactive dashboard. 


**/scrapers:** Python modules for extracting government nutritional data. 


**/api_handlers:** Scripts managing Yelp Fusion API requests and location harvesting. 


**/analysis:** Jupyter notebooks containing exploratory data analysis (EDA) and hypothesis testing. 


**requirements.txt:** List of dependencies required to run the application locally or in the cloud.

## PM Note: The "Dirty Bulk" Insight
"This project was driven by a desire to validate 'gym talk' with objective data. By merging nutritional density from government sources with live Yelp location data, I was able to model how a lifter's immediate environment impacts their performance outcomes. It demonstrates my ability to take a niche behavioral hypothesis and build a technical pipeline to test it."
