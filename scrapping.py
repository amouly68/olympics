
import pandas as pd

#import data from local csv file 


medals = pd.read_csv('medals.csv')
athletes = pd.read_csv('athlete_events.csv')
regions = pd.read_csv('noc_regions.csv')



athletes.describe() 


medals.head()
athletes.head()
regions.head()

