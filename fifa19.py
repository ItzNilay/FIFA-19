import pandas as pd

fifa_data = pd.read_csv('fifa19.csv')

# Get some basic information about the dataset
print("Number of rows : ", len(fifa_data))
print("Number of columns : ", len(fifa_data.columns))
print("\n")

# Display the first 10 rows of the dataset
print("First 10 rows of the dataset :")
print(fifa_data.head(10))
print("\n")

# Display some basic statistics for the 'Overall' column
print("Basic statistics for the 'Overall' column :")
print(fifa_data['Overall'].describe())
print("\n")

# Count the number of players by nationality
nationality_counts = fifa_data['Nationality'].value_counts()
print("Number of players by nationality :")
print(nationality_counts)
print("\n")

# Count the number of players by club
club_counts = fifa_data['Club'].value_counts()
print("Number of players by club:")
print(club_counts)
print("\n")

# Display the average age of players by nationality
avg_age_by_nationality = fifa_data.groupby('Nationality')['Age'].mean()
print("Average age of players by nationality :")
print(avg_age_by_nationality)
print("\n")

# Display the average rating of players by club
avg_rating_by_club = fifa_data.groupby('Club')['Overall'].mean()
print("Average rating of players by club :")
print(avg_rating_by_club)
print("\n")

# Display the average cost of players by club
avg_cost_by_club = fifa_data.groupby('Cost')['Overall'].mean()
print("Average cost of players by club :")
print(avg_cost_by_club)
print("\n")

# Display the stadiums by club
stadiums_by_clubs = fifa_data.groupby('Stadiums')['Overall'].mean()
print("List of Clubs' stadiums :")
print(stadiums_by_clubs)
print("\n")

# Display the Coaches of each club
Coaches_clubs = fifa_data.groupby('Coaches')['Overall'].mean()
print("Coaches of each club :")
print(Coaches_clubs)
print("\n")

# Display the Captains of each club
Captains_clubs = fifa_data.groupby('Captains')['Overall'].mean()
print("Captains of each club :")
print(Captains_clubs)
print("\n")

# Titles or Victories of each club
Titles_clubs = fifa_data.groupby('Titles')['Overall'].mean()
print("Titles of each club :")
print(Titles_clubs)
print("\n")
