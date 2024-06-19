
import pandas as pd

#import data from local csv file 


medals = pd.read_csv('medals.csv')
athletes = pd.read_csv('Data/120years/athlete_events.csv')
regions = pd.read_csv('Data/120years/noc_regions.csv')

ath_bio = pd.read_csv('Data/Olympedia/Olympic_Athlete_Bio.csv')
ath_event = pd.read_csv('Data/Olympedia/Olympic_Athlete_Event_Results.csv')
game_medals = pd.read_csv('Data/Olympedia/Olympic_Games_Medal_Tally.csv')
results = pd.read_csv('Data/Olympedia/Olympic_Results.csv')
country = pd.read_csv('Data/Olympedia/Olympics_Country.csv')
games = pd.read_csv('Data/Olympedia/Olympics_Games.csv')



athletes.describe() 
ath_bio.head()
ath_event.head()
games.head()
games.tail()
tokyo = games[games['city'] == 'Tokyo']
tokyo.head()
ath_tokyo = ath_event[ath_event['edition_id'] == 61]
ath_tokyo.head()

medals.head()
athletes.head()
regions.head()

