
import pandas as pd

# Read the CSV file
data = pd.read_csv('pop_gdp.csv')
data.head()


games = pd.read_csv('Olympics_Games.csv')
games.head()
years = games['year'].unique()

# keep only the years that are in the data

data_ol_year= data[data['year'].isin(years)]

data_ol_year.head()

