import re
import pandas as pd

# Read the CSV file
df = pd.read_csv('Olympic_Athlete_Bio.csv')
df.head()
df.describe()
df.info()


def parse_date(born):
    if pd.isnull(born):
        return None, None, None
    
    # Nettoyer les caractères indésirables
    born = born.strip("()")

    parts = born.split()
    day, month, year = None, None, None
    
    if len(parts) == 3:
        day, month, year = parts[0], parts[1], parts[2]
    elif len(parts) == 2:
        if parts[0].isdigit() and len(parts[0]) == 4:  # Cas où il n'y a que l'année
            year = parts[0]
        else:
            month, year = parts[0], parts[1]
    elif len(parts) == 1 and parts[0].isdigit() and len(parts[0]) == 4:
        year = parts[0]
    
     # Si la date n'est pas dans le format standard, tenter de trouver l'année dans un texte plus long
    if year is None:
        match = re.search(r'\b(18|19|20)\d{2}\b', born)
        if match:
            year = match.group(0)


    # Convertir les jours et les années en entiers
    if day is not None and day.isdigit():
        day = int(day)
    if year is not None and year.isdigit():
        year = int(year)
    
    # Mapper les mois à des entiers
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }
    if month in months:
        month = months[month]
    
    return day, month, year

# Appliquer la fonction pour séparer les dates
new_df = df.copy()
new_df[['DoB_day', 'DoB_month', 'DoB_year']] = df['born'].apply(lambda x: pd.Series(parse_date(x)))


# Appliquer la fonction pour corriger les dates mal formatées
def correct_year_in_day(df):
    for index, row in df.iterrows():
        if isinstance(row['DoB_day'], int) and row['DoB_day'] > 1000:
            df.at[index, 'DoB_year'] = row['DoB_day']
            df.at[index, 'DoB_day'] = None
        elif isinstance(row['DoB_day'], str) and row['DoB_day'].isdigit() and int(row['DoB_day']) > 1000:
            df.at[index, 'DoB_year'] = int(row['DoB_day'])
            df.at[index, 'DoB_day'] = None

# Appliquer la fonction pour corriger les dates
correct_year_in_day(new_df)


# Compter les valeurs nulles et non-string avant transformation pour information
null_values_count = df['born'].isnull().sum()
null_values_count_na = df['born'].isna().sum()
non_string_values_count = df['born'].apply(lambda x: not isinstance(x, str)).sum()

print(f"Number of null values in 'born': {null_values_count}")
print(f"Number of non-string values in 'born': {non_string_values_count}")

# valeurs nulles dans new_df
null_values_count = new_df['born'].isnull().sum()
non_string_values_count = new_df['born'].apply(lambda x: not isinstance(x, str)).sum()

print(f"Number of null values in 'born': {null_values_count}")
print(f"Number of non-string values in 'born': {non_string_values_count}")




new_df.head(100)



# Convertir les colonnes en int
# Convertir DAY
print(new_df['DoB_day'].unique())
print(new_df['DoB_day'].value_counts())
problematic_rows = new_df[new_df['DoB_day'] == 'in']
problematic_rows = problematic_rows[['DoB_day', 'born']]
print(problematic_rows)
new_df.loc[new_df['DoB_day'] == 'in', 'DoB_day'] = pd.NA
new_df['DoB_day'] = new_df['DoB_day'].replace([None, 'nan', pd.NaT], pd.NA)
null_day_count = new_df['DoB_day'].isna().sum()

# ok pour day
new_df['DoB_day'] = new_df['DoB_day'].astype(pd.Int64Dtype())

# convertir MONTH
print(new_df['DoB_month'].unique())
print(new_df['DoB_month'].value_counts())
problematic_rows = new_df[new_df['DoB_month'].isin(['?', 'Scotland', 'c.'])]
problematic_rows = problematic_rows[['DoB_day','DoB_month', 'DoB_year', 'born', 'country']]
print(problematic_rows)
new_df.loc[new_df['DoB_month'].isin(['?', 'Scotland']), 'DoB_year'] = pd.NA
new_df['DoB_month'] = new_df['DoB_month'].replace(['?', 'c.', 'Scotland'], pd.NA)
problematic_rows = new_df[new_df['DoB_month'] == 'or']
problematic_rows = problematic_rows[['DoB_day','DoB_month', 'DoB_year', 'born', 'country']]
print(problematic_rows)
new_df['DoB_month'] = new_df['DoB_month'].replace(['or', 'circa'], pd.NA)
new_df['DoB_month'] = new_df['DoB_month'].replace([None, 'nan', pd.NaT], pd.NA)


new_df['DoB_month'] = new_df['DoB_month'].astype(pd.Int64Dtype())



# convertir YEAR
print(new_df['DoB_year'].unique())
print(new_df['DoB_year'].value_counts())
new_df['DoB_year'] = new_df['DoB_year'].replace([None, 'nan', pd.NaT], pd.NA)
new_df['DoB_year'] = new_df['DoB_year'].astype(pd.Int64Dtype())


#compare null born and null [ day, month, year]
null_born_count = new_df['born'].isna().sum()
null_day_month_year_count = new_df[['DoB_day', 'DoB_month', 'DoB_year']].isna().sum()

print(f"Number of null values in 'born': {null_born_count}")
print(f"Number of null values in 'DoB_day', 'DoB_month', 'DoB_year': {null_day_month_year_count}")

#check born not null and year  null
problematic_rows = new_df[(~new_df['born'].isna()) & (new_df['DoB_year'].isna())]
problematic_rows = problematic_rows[[ 'born', 'DoB_year', 'DoB_month', 'DoB_day']]
with open('problematic_rows.txt', 'w') as f:
    problematic_rows.to_string(f, index=False)

#check born not null and month null
problematic_rows = new_df[(~new_df['born'].isna()) & (new_df['DoB_month'].isna())]
problematic_rows = problematic_rows[[ 'born', 'DoB_year', 'DoB_month', 'DoB_day']]
print (problematic_rows)
with open('problematic_rows2.txt', 'a') as f:
    problematic_rows.to_string(f, index=False)

#check born not null and day null
problematic_rows = new_df[(~new_df['born'].isna()) & (~new_df['DoB_month'].isna()) & (new_df['DoB_day'].isna())]
problematic_rows = problematic_rows[[ 'born', 'DoB_year', 'DoB_month', 'DoB_day']]
print (problematic_rows)
with open('problematic_rows3.txt', 'a') as f:
    problematic_rows.to_string(f, index=False)


# Supprimer les lignes avec des dates mal formatées


# Supprimer la colonne 'born'

new_df.head(100)


df.head()