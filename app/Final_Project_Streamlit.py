import streamlit as st
import sqlite3
import pandas as pd

# Intro page
def page_intro():
    st.title("The Correlation of Fast Food Nutrition Availability on Powerlifting Performance")
    st.write("1. Name:")
    st.write("Yun Cheih (Jack) Lee")
    st.write("2. An explanation of how to use your webapp: what interactivity there is, what the plots/charts mean, what your conclusions were, etc.: ")
    st.write("The web app I built features three final compacted dataframes. The first page compares either the squat/bench/deadlift/total to the average macronutrient density of a fastfood chain's menu. The second page does something similar, but compares the dots score instead. For context, dots score is another rating for powerlifting that accounts for the lifter's bodyweight relative to the total weight they moved. The last one is a broader view of performance grouped by state instead of fast food chain.")
    st.write("My app also offers some interactivity with filters on the sidebar. Some of it just to trim down the datasize to look at certain populations, while I also have filters for choosing a specific powerlifting movement vs. a specific macronutrient so that the user can dive into more specifics rather than an overarching view. ")
    st.write("The interactivity allows the user to look at specific components of data on each page. On chart page 1, we have the dataset grouped by proximity to Fast Food Chains. The user could see if there are any differences across squat/bench/deadlit/total or if maybe gender has an impact on performance relative to the fast food chains.")
    st.write("The second chart page is very similar in interactivity, but takes the dots score as a comparison instead of a particular lift(dot score is a rating relative to body weight). Both of these pages also still offer other filters like whether it was a drug tested meet or if it was a raw/equipped meet.")
    st.write("The final page is the dataset but broken down instead by state. I thought this would just be interesting to see how performance in strength may have varied across different states.")
    st.write("3. Major Gotchas: ")
    st.write("I think the toughest component of the project for me was webscraping as a whole without much experience prior in html. I think the prior lab we had done on webscraping really undersold how tough it would actually be-- working with a website designed to be scraped is far, and I mean far easier than a site that does not want to be scraped.")
    st.write("I also started my project with a much larger scope not realizing how difficult that would be with my current skills with coding/data science. I wanted to cover all restaurants which would have been nearly impossible to get menus to tie together for each location.")
    st.write("As for technical expertise, I broke my scripts apart into multiple components and the use of CSVs just because it was a format I was more familiar working with. I think the reality is that these could be combined and done in a smoother fashion if I had more experience working with python and the pandas library(as well as just operating sqlite through python).")
    st.write("The last major gotcha that really forced me to stay up late today on 05/02/2024 was not realizing the sheer size of my database. I had to trim it down from the 19million rows by aggregating things into averages and moving it into a csv file so that I could actually upload it onto GitHub to deploy.")


# Analysis results page
def page_data_analysis():
    st.title("Page 2: Data Analysis")
    st.write("1. What did you set out to study?  (i.e. what was the point of your project?  This should be close to your Milestone 1 assignment, but if you switched gears or changed things, note it here.): ")
    st.write("My data analysis was designed to study a correlational relationship between available fast food chains and a strength sport (powerlifting). I started with wanting to look at availability of all foods within a competition's area, but it was simply too hard to aggregate all the possible menus across the restaurants all over the United States. I determined the most 'available' fast food chain in each area by counting the number of them, and then chose the one with the most reviews if there was a tie for count. To delve deeper into nutritional impact of fast food availability, I webscraped fast food nutritional data to see if that had any impact on the trends noticed.")
    st.write("One of the main assumptions was that people were very likely to eat out because of traveling to different locations. Fast food is the most consistent across many different areas, so I hypothesized that competitors had a high likeliness to eat at fastfood restaurants during or around the time of their meet. I wanted to explore if there was any potential correlation of this with their actual strength performance on meet day.")
    st.write("2. What did you Discover/what were your conclusions (i.e. what were your findings?  Were your original assumptions confirmed, etc.?): ")
    st.write("My original assumption was that areas with higher protein fast foods might would have higher powerlifting totals or dot scores because of the link between protein and muscle building as well as powerlifters being notoriously known as strong people with bad diets (hence why they can't do bodybuilding)")
    st.write("My data shows that powerlifting as a sport seems to have increased in general strength/avg strength over the years, but no correlation was shown in regards to a correlation to the most available fast food to a certain meet location. My original assumptions proved to be untrue.")
    st.write("Some other fairly obvious results that I noticed were that performance was much better for untested lifters because of the more likely steroid usage, male lifters having much higher lift averages than female lifters, and the spike in strength as people are in their 20s/30s.")
    st.write("However, if I had more menu data for more restaurants in an area, we may be able to compare the nutrition in a general area to strength performance and reevaluate the original assumption with a larger sample of food items accessible within a meet area.")
    st.write("3. What difficulties did you have in completing the project?: ")
    st.write("The major difficulty I struggled with was coming up with an idea and somehow looking for 2 other data sets that we had to acquire in very specific manners to fit with my original idea.")
    st.write("I'm hoping that exploratory data analyses like these in the real world won't require me to specifically webscrape one source and use an api for another source. Ideally, those would still appear but I wouldn't be limited to specifically needing to do one of each of those to fulfill a project criteria.")
    st.write("I also struggled a lot with putting together a small enough file that could be uploaded onto GitHub's repository to deploy this web app. I did not realize the limitations that it had and had to scale my project down during the last two days.")
    st.write("4. What skills did you wish you had while you were doing the project?: ")
    st.write("During the duration of this project, I really wish I simply had a better grasp on data engineering as a whole. I have worked on large SQL servers with many tables before without having a proper grasp on how difficult it was to actually create the infrastructure going into it. I used SQL in previous jobs without a true appreciation for the engineers and architects that put together a scalable model and system to be used across multiple departments within a company.")
    st.write("As I had mentioned in my gotchas, I wish I had much more experience with webscraping. I did not realize how many websites in the modern day and age are actively working against you to be webscraped. While I understand why they choose to protect their sites in that manner, the modern environment does make it a little bit tougher for new learners to actually learn and practice webscraping. I though webscraping was a simple task from the labs until I had to really try and webscrape for this project.")
    st.write("5. What would you do “next” to expand or augment the project?: ")
    st.write("My current project looks at nutritional data and performs an analysis based on the average values. To expand on this project, I would love to have either data on specific athlete training cycles or the actual frequency of certain items being ordered at each individual fast food chain. The first augment would just purely be for my interest on maybe most effective ways to strength train, while the second augment I mentioned could help dial in on the fast food further and make adjustments to the weight of different food items based on how often they are ordered relative to other food items instead of averaging (which assumes the distribution of ordering is uniform).")
    st.write("I think as I get more experienced with data science, I could actually recyle the dataset to also predict maybe which competitors are likely to place or win in the larger meets like Sheffield. It would be interesting to apply data science techniques to make models predicing performance and meet outcomes.")

def get_state_options():
    df = pd.read_csv('powerlifting_data_shrunk.csv')
    
    # unique states options from the 'MeetState' column
    state_options = df['MeetState'].unique().tolist()
    
    return state_options

def page_data_table1():
    # parameters for my sidebar based on dataset
    lifts_options = ['AvgBest3SquatKg', 'AvgBest3BenchKg', 'AvgBest3DeadliftKg', 'AvgTotalKg'] 
    min_year = 2019 
    max_year = 2024
    min_age = 0
    max_age = 96
    gender_options = ['M', 'F']
    nutrient_options = ['AvgProtein', 'AvgFat', 'AvgCarbohydrates']
    test_options = ['Yes', 'No']
    equipment_options = ['Raw', 'Not Raw']
    state_options = get_state_options()

    st.title("Page 3: Data By Fast Food Chain (Lifts)")

    #sidebar and the filters on it
    st.sidebar.header('Filters')
    lifts_input = st.sidebar.selectbox('Select Lift: ', lifts_options, index=0)
    year_range = st.sidebar.slider('Select Year Range: ', min_value=min_year, max_value=max_year, value=(min_year, max_year))
    age_range = st.sidebar.slider('Select Age Range: ', min_value=min_age, max_value=max_age, value=(min_age, max_age))
    gender_input = st.sidebar.multiselect('Select Genders: ', gender_options, default=gender_options)
    nutrient_input = st.sidebar.selectbox('Select Macronutrient: ', nutrient_options, index=0)
    tested_input = st.sidebar.multiselect('Select Tested or Not: ', test_options, default=test_options)
    equipment_input = st.sidebar.multiselect('Select Equipment: ', equipment_options, default=equipment_options)
    state_input = st.sidebar.multiselect('Select States: ', state_options, default=state_options)

    df = pd.read_csv('powerlifting_data_shrunk.csv')

    # data filters from sidebar
    mask = (
        (pd.to_datetime(df['Date']).dt.year >= year_range[0]) & 
        (pd.to_datetime(df['Date']).dt.year <= year_range[1]) &
        (df['Age'] >= age_range[0]) & 
        (df['Age'] <= age_range[1]) &
        (df['Sex'].isin(gender_input)) &
        (df['MeetState'].isin(state_input)) &
        ((df['Tested'].isin(tested_input)) | df['Tested'].isnull())
    )
    # equipment usage filter
    if 'Raw' in equipment_input:
        mask &= (df['Equipment'] == 'Raw')
    elif 'Not Raw' in equipment_input:
        mask &= (df['Equipment'] != 'Raw')

    filtered_df = df[mask]

    # grouping by name 
    grouped_df = filtered_df.groupby('FastFoodName').agg({
        lifts_input: 'mean',
        nutrient_input: 'mean'
    }).reset_index()

    st.write(grouped_df)

    #plot 1 comparing nutrients to lifting
    st.write("Weight lifted vs. Nutrition Scatter Plot")
    st.scatter_chart(data=grouped_df, x=lifts_input, y=nutrient_input, use_container_width=True)

def page_data_table2():
    # parameters for my sidebar based on dataset
    min_year = 2019 
    max_year = 2024
    min_age = 0
    max_age = 96
    gender_options = ['M', 'F']
    nutrient_options = ['AvgProtein', 'AvgFat', 'AvgCarbohydrates']
    test_options = ['Yes', 'No']
    equipment_options = ['Raw', 'Not Raw']
    state_options = get_state_options()

    st.title("Page 4: Data By Fast Food Chain (Dots)")

    #sidebar and the filters on it
    st.sidebar.header('Filters')
    year_range = st.sidebar.slider('Select Year Range: ', min_value=min_year, max_value=max_year, value=(min_year, max_year))
    age_range = st.sidebar.slider('Select Age Range: ', min_value=min_age, max_value=max_age, value=(min_age, max_age))
    gender_input = st.sidebar.multiselect('Select Genders: ', gender_options, default=gender_options)
    nutrient_input = st.sidebar.selectbox('Select Macronutrient: ', nutrient_options, index=0)
    tested_input = st.sidebar.multiselect('Select Tested or Not: ', test_options, default=test_options)
    equipment_input = st.sidebar.multiselect('Select Equipment: ', equipment_options, default=equipment_options)
    state_input = st.sidebar.multiselect('Select States: ', state_options, default=state_options)

    df = pd.read_csv('powerlifting_data_shrunk.csv')

    # data filters from sidebar
    mask = (
        (pd.to_datetime(df['Date']).dt.year >= year_range[0]) & 
        (pd.to_datetime(df['Date']).dt.year <= year_range[1]) &
        (df['Age'] >= age_range[0]) & 
        (df['Age'] <= age_range[1]) &
        (df['Sex'].isin(gender_input)) &
        (df['MeetState'].isin(state_input)) &
        ((df['Tested'].isin(tested_input)) | df['Tested'].isnull())
    )
    # equipment usage filter
    if 'Raw' in equipment_input:
        mask &= (df['Equipment'] == 'Raw')
    elif 'Not Raw' in equipment_input:
        mask &= (df['Equipment'] != 'Raw')

    filtered_df = df[mask]

    # grouping by name (of fast food restaurant)
    grouped_df = filtered_df.groupby('FastFoodName').agg({
        'AvgDots': 'mean',
        nutrient_input: 'mean'
    }).reset_index()

    st.write(grouped_df)

    # plot of nutrients vs Average Dots
    st.write("Dots Score vs. Nutrition Scatter Plot")
    st.scatter_chart(data=grouped_df, x='AvgDots', y=nutrient_input, use_container_width=True)

def page_data_table3():
    # parameters for the sidebar based on dataset
    min_year = 2019 
    max_year = 2024
    min_age = 0
    max_age = 96
    gender_options = ['M', 'F']
    nutrient_options = ['AvgProtein', 'AvgFat', 'AvgCarbohydrates']
    test_options = ['Yes', 'No']
    equipment_options = ['Raw', 'Not Raw']
    state_options = get_state_options()

    st.title("Page 5: Data By States")

    # Sidebar and the filters on it
    st.sidebar.header('Filters')
    year_range = st.sidebar.slider('Select Year Range: ', min_value=min_year, max_value=max_year, value=(min_year, max_year))
    age_range = st.sidebar.slider('Select Age Range: ', min_value=min_age, max_value=max_age, value=(min_age, max_age))
    gender_input = st.sidebar.multiselect('Select Genders: ', gender_options, default=gender_options)
    nutrient_input = st.sidebar.selectbox('Select Macronutrient: ', nutrient_options, index=0)
    tested_input = st.sidebar.multiselect('Select Tested or Not: ', test_options, default=test_options)
    equipment_input = st.sidebar.multiselect('Select Equipment: ', equipment_options, default=equipment_options)
    state_input = st.sidebar.multiselect('Select States: ', state_options, default=state_options)

    df = pd.read_csv('powerlifting_data_shrunk.csv')

    # Data filters from sidebar
    mask = (
        (pd.to_datetime(df['Date']).dt.year >= year_range[0]) & 
        (pd.to_datetime(df['Date']).dt.year <= year_range[1]) &
        (df['Age'] >= age_range[0]) & 
        (df['Age'] <= age_range[1]) &
        (df['Sex'].isin(gender_input)) &
        (df['MeetState'].isin(state_input)) &
        ((df['Tested'].isin(tested_input)) | df['Tested'].isnull())
    )
    # Equipment usage filter
    if 'Raw' in equipment_input:
        mask &= (df['Equipment'] == 'Raw')
    elif 'Not Raw' in equipment_input:
        mask &= (df['Equipment'] != 'Raw')

    filtered_df = df[mask]

    # Grouping by state
    grouped_df = filtered_df.groupby('MeetState').agg({
        'AvgBest3SquatKg': 'mean',
        'AvgBest3BenchKg': 'mean',
        'AvgBest3DeadliftKg': 'mean',
        'AvgTotalKg': 'mean',
        nutrient_input: 'mean'
    }).reset_index()

    st.write(grouped_df)

    # Plot to compare weight to nutrients, except grouped by state average
    st.write("Total Weight Lifted vs. Nutrition Scatter Plot by State")
    st.scatter_chart(data=grouped_df, x='AvgTotalKg', y=nutrient_input, use_container_width=True)

    # Bar chart to compare total weight lifted by state
    st.write("Total Weight Lifted by State")
    st.bar_chart(data=grouped_df, x='MeetState', y='AvgTotalKg')

# For choosing pages
page = st.sidebar.selectbox("Choose a Page", ["Introduction", "Data Analysis Results", "Data Table 1", "Data Table 2", "Data Table 3"])

if page == "Introduction":
    page_intro()
elif page == "Data Analysis Results":
    page_data_analysis()
elif page == "Data Table 1":
    page_data_table1()
elif page == "Data Table 2":
    page_data_table2()
else:
    page_data_table3()
