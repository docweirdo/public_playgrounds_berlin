import pandas as pd

lors = pd.read_csv('../assets/lor_2021.csv', sep=';', index_col='PLR_id')
children = pd.read_csv('../assets/children_06_2022.csv', sep=',', index_col='PLR')
lors_playgrounds = pd.read_csv('../assets/lor_playgrounds.csv', sep=',', encoding='utf-8', index_col='PLR_id')
playgrounds = pd.read_excel('../assets/playgrounds.xls', index_col='id')

# drop non accredible playgrounds, set total area for playable area for missing values
playgrounds = playgrounds[playgrounds['anrechenbar Spielplatzversorgung']].drop(['anrechenbar Spielplatzversorgung'], axis=1)
playgrounds['playground_area'] = playgrounds['Nettospielfläche in m²']
playgrounds['playground_area'] = playgrounds.apply(lambda row: row['Größe in m² (Kataster)'] if isinstance(row['playground_area'], str) else row['playground_area'], axis=1)
playgrounds.drop(['Größe in m² (Kataster)', 'Nettospielfläche in m²'], axis=1, inplace=True)
playgrounds.index.names = ['playground_id']

print(playgrounds)

lors_playgrounds = lors_playgrounds.join(playgrounds, on='playground_id').drop('PLR_id', axis=1)

# count playgrounds within Lor
agg_funcs = {'playground_id': 'count', 'playground_area': 'sum'}
lors[['playground_count', 'playground_area']] = lors_playgrounds[['playground_id', 'playground_area']].groupby('PLR_id').aggregate(agg_funcs)

# if no association could be made, row is NaN, fill with 0 playgroudds
lors['playground_count'].fillna(0, inplace=True)
lors['playground_area'].fillna(0, inplace=True)

print(lors)
