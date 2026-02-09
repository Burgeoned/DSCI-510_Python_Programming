import pandas as pd
import sqlite3

#location table to reference other tables on
def create_location_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS locations (
                    id INTEGER PRIMARY KEY,
                    State TEXT,
                    City TEXT,
                    UNIQUE(State, City)
                    )''')

def insert_location(conn, state, city):
    try:
        conn.execute("INSERT OR IGNORE INTO locations (State, City) VALUES (?, ?)", (state, city))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Duplicate entry ignored for {state}, {city}")

#powerlifting table based on canned CSV
def create_openpowerlifting_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS openpowerlifting (
                    id INTEGER PRIMARY KEY,
                    Name TEXT,
                    Sex TEXT,
                    Event TEXT,
                    Equipment TEXT,
                    Age FLOAT,
                    AgeClass TEXT,
                    BirthYearClass TEXT,
                    Division TEXT,
                    BodyweightKg FLOAT,
                    WeightClassKg TEXT,
                    Squat1Kg FLOAT,
                    Squat2Kg FLOAT,
                    Squat3Kg FLOAT,
                    Squat4Kg FLOAT,
                    Best3SquatKg FLOAT,
                    Bench1Kg FLOAT,
                    Bench2Kg FLOAT,
                    Bench3Kg FLOAT,
                    Bench4Kg FLOAT,
                    Best3BenchKg FLOAT,
                    Deadlift1Kg FLOAT,
                    Deadlift2Kg FLOAT,
                    Deadlift3Kg FLOAT,
                    Deadlift4Kg FLOAT,
                    Best3DeadliftKg FLOAT,
                    TotalKg FLOAT,
                    Place TEXT,
                    Dots FLOAT,
                    Wilks FLOAT,
                    Glossbrenner FLOAT,
                    Goodlift FLOAT,
                    Tested TEXT,
                    Country TEXT,
                    State TEXT,
                    Federation TEXT,
                    ParentFederation TEXT,
                    Date TEXT,
                    MeetCountry TEXT,
                    MeetState TEXT,
                    MeetTown TEXT,
                    MeetName TEXT,
                    Sanctioned TEXT,
                    location_id INTEGER,
                    FOREIGN KEY (location_id) REFERENCES locations(id)
                    )''')

def insert_powerlifting_record(conn, row, location_id):
    conn.execute('''INSERT INTO openpowerlifting (
                    Name, Sex, Event, Equipment, Age, AgeClass, BirthYearClass, Division, BodyweightKg,
                    WeightClassKg, Squat1Kg, Squat2Kg, Squat3Kg, Squat4Kg, Best3SquatKg, Bench1Kg, Bench2Kg,
                    Bench3Kg, Bench4Kg, Best3BenchKg, Deadlift1Kg, Deadlift2Kg, Deadlift3Kg, Deadlift4Kg,
                    Best3DeadliftKg, TotalKg, Place, Dots, Wilks, Glossbrenner, Goodlift, Tested, Country,
                    State, Federation, ParentFederation, Date, MeetCountry, MeetState, MeetTown, MeetName,
                    Sanctioned, location_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                    (row['Name'], row['Sex'], row['Event'], row['Equipment'], row['Age'], row['AgeClass'],
                    row['BirthYearClass'], row['Division'], row['BodyweightKg'], row['WeightClassKg'], row['Squat1Kg'],
                    row['Squat2Kg'], row['Squat3Kg'], row['Squat4Kg'], row['Best3SquatKg'], row['Bench1Kg'],
                    row['Bench2Kg'], row['Bench3Kg'], row['Bench4Kg'], row['Best3BenchKg'], row['Deadlift1Kg'],
                    row['Deadlift2Kg'], row['Deadlift3Kg'], row['Deadlift4Kg'], row['Best3DeadliftKg'], row['TotalKg'],
                    row['Place'], row['Dots'], row['Wilks'], row['Glossbrenner'], row['Goodlift'], row['Tested'],
                    row['Country'], row['State'], row['Federation'], row['ParentFederation'], row['Date'],
                    row['MeetCountry'], row['MeetState'], row['MeetTown'], row['MeetName'], row['Sanctioned'],
                    location_id))
    conn.commit()

def main():
    try:
        # Read openpowerlifting.csv
        dtype_options = {'State': 'str', 'ParentFederation': 'str', 'MeetState': 'str'} 
        powerlifting_df = pd.read_csv("openpowerlifting.csv", dtype=dtype_options)

        # Filtering the df for the data I want in my table for my project scope
        filtered_df = powerlifting_df[(powerlifting_df['Date'] >= '2019-01-01') &  # meet_date in 2019 or later (past 5 years)
                                    (powerlifting_df['MeetCountry'] == 'USA') &  # meet_country USA only
                                    (powerlifting_df['Sanctioned'] == 'Yes') &  # Sanctioned = Yes (official meet)
                                    (powerlifting_df['Event'] == 'SBD')]  # Event = SBD (squat bench and deadlift included)

        conn = sqlite3.connect('powerlifting_data.db')

        # Create location table
        create_location_table(conn)

        # Create openpowerlifting table
        create_openpowerlifting_table(conn)

        # Iterating over filtered data to insert locations into the location table and powerlifting records
        for i, row in filtered_df.iterrows():
            state = row['MeetState']
            city = row['MeetTown']

            # location id 9999 to catch cases of not valid combo of state and city
            if pd.isnull(state) or pd.isnull(city):
                location_id = 9999
            else:
                insert_location(conn, state, city)

                # Get location_id for the current row
                location_id_result = conn.execute("SELECT id FROM locations WHERE State = ? AND City = ?", (state, city)).fetchone()
                if location_id_result:
                    location_id = location_id_result[0]
                else:
                    print(f"No location found for state: {state} and city: {city}")
                    continue

            insert_powerlifting_record(conn, row, location_id)
        print("Data inserted successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
