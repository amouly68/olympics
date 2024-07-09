
import pandas as pd

# Read the CSV file
data = pd.read_csv('Olympic_Athlete_Event_Results.csv')
data.head()
test_riner = data[data['athlete_id'] == 112724]
print (test_riner)


data_medal = pd.read_csv('Olympic_Games_Medal_Tally.csv')
data_medal.head()


data_results = pd.read_csv('Olympic_Results.csv')
data_results.head()
test_results = data_results[data_results['result_id'].isin([260537, 316678, 354880, 18001172, 18000780])]
with open('test.txt', 'a') as f:
    test_results.to_string(f, index=False)


data_results.describe()
data_results.info()


games = pd.read_csv('Olympics_Games.csv')



