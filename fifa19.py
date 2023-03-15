import pandas as pd

# Load the dataset
fifa_data = pd.read_csv('fifa19.csv')

# Get some basic information about the dataset
print("Number of rows: ", len(fifa_data))
print("Number of columns: ", len(fifa_data.columns))
print("\n")

# Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(fifa_data.head())
print("\n")

# Display some basic statistics for the 'Overall' column
print("Basic statistics for the 'Overall' column:")
print(fifa_data['Overall'].describe())
print("\n")

# Count the number of players by nationality
nationality_counts = fifa_data['Nationality'].value_counts()
print("Number of players by nationality:")
print(nationality_counts)
print("\n")

# Count the number of players by club
club_counts = fifa_data['Club'].value_counts()
print("Number of players by club:")
print(club_counts)
print("\n")

# Display the average age of players by nationality
avg_age_by_nationality = fifa_data.groupby('Nationality')['Age'].mean()
print("Average age of players by nationality:")
print(avg_age_by_nationality)
print("\n")

# Display the average rating of players by club
avg_rating_by_club = fifa_data.groupby('Club')['Overall'].mean()
print("Average rating of players by club:")
print(avg_rating_by_club)
print("\n")
