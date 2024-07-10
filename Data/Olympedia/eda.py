
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
countries = data_ol_year['country'].unique()

print([country for country in countries if "livia" in country])
print(data_ol_year[data_ol_year['country'].str.contains("livia")])


country_noc = pd.read_csv('Olympics_Country.csv')

country_noc.head()

countries_noc = country_noc['country'].unique()
print([country for country in countries_noc if "livia" in country])
print(country_noc[country_noc['country'].str.contains("livia")])

diff = set(countries) - set(countries_noc)
diff = sorted(diff)
print(diff)

#list of countries wherw "olivia" is ine the name



diff2 = set(countries_noc) - set(countries)
diff2 = sorted(diff2)
print(diff2)

test = pd.merge(data_ol_year, country_noc, left_on='country', right_on='country', how='left', suffixes=('_data', '_noc'))
test.head()
countries_after_merge = test['country'].unique()
test = pd.merge(test, country_noc, left_on='countrycode', right_on='noc', how='outer', suffixes=('_data', '_noc'))
test.head()

#check where counrty_noc is diffrent from country_data and noc_data is equal to noc_noc (unique values)
diff3 = test[(test['country_data'].isna())]
diff3.head()
algeria = test[test['country'] == 'Algeria']
algeria.head()
boli = test[test['countrycode'] == 'BOL']
boli.head()

noc_na = test[(test['noc'].isna())]
noc_na.head()
noc_nan= noc_na[['countrycode', 'country']]
noc_nan = noc_nan.drop_duplicates()
merge = pd.merge(noc_nan, country_noc, left_on='countrycode', right_on='noc', how='left', suffixes=('_data', '_noc'))
merge.head(25)
merge_right = pd.merge(noc_nan, country_noc, left_on='countrycode', right_on='noc', how='right', suffixes=('_data', '_noc'))
merge_right.head(25)
