import pandas as pd
import seaborn as sns
import matplotlib as mpl

sns.set_theme()

lors = pd.read_csv('../assets/lor_2021.csv', sep=';', index_col='PLR_id', usecols=['PLR_id', 'PLR_name', 'area_sqm'])
childpoverty= pd.read_csv('../assets/childpoverty_202012.csv', sep='|', index_col='PLR_id', usecols=['PLR_id', 'poverty', 'comment'])
population = pd.read_csv('../assets/children_06_2021.csv', sep=',', encoding='utf-8', index_col='PLR_id')
lors_playgrounds = pd.read_csv('../assets/lor_playgrounds.csv', sep=',', encoding='utf-8', index_col='PLR_id')
playgrounds = pd.read_excel('../assets/playgrounds.xls', index_col='id', usecols=['id', 'anrechenbar Spielplatzversorgung', 'Nettospielfläche in m²', 'Größe in m² (Kataster)'])

# drop non accredible playgrounds, set total area for playable area for missing values
playgrounds = playgrounds[playgrounds['anrechenbar Spielplatzversorgung']].drop(['anrechenbar Spielplatzversorgung'], axis=1)
playgrounds['playground_area'] = playgrounds['Nettospielfläche in m²']
playgrounds['playground_area'] = playgrounds.apply(lambda row: row['Größe in m² (Kataster)'] if isinstance(row['playground_area'], str) else row['playground_area'], axis=1)
playgrounds.drop(['Größe in m² (Kataster)', 'Nettospielfläche in m²'], axis=1, inplace=True)
playgrounds.index.names = ['playground_id']

# drop invalid districts for childpoverty, change datatype for poverty
childpoverty = childpoverty[childpoverty['comment'] == 'gültig'].drop(['comment'], axis=1)
childpoverty['poverty'] = childpoverty['poverty'].str.replace(',', '.').astype(float)


# aggregate children
population['total_children'] = population['<6'] + population['6-15'] + population['15-18']

lors_playgrounds = lors_playgrounds.join(playgrounds, on='playground_id')

# count playgrounds within Lor
agg_funcs = {'playground_id': 'count', 'playground_area': 'sum'}
lors[['playground_count', 'playground_area']] = lors_playgrounds[['playground_id', 'playground_area']].groupby('PLR_id').aggregate(agg_funcs)

# if no association could be made, row is NaN, fill with 0 playgrounds respective area
lors['playground_count'].fillna(0, inplace=True)
lors['playground_area'].fillna(0, inplace=True)

childpoverty = childpoverty.join(population[['total_population', 'total_children']])
#childpoverty['poor_children'] = childpoverty['total_children'] * childpoverty['poverty'] / 100

lors = lors.join(childpoverty)

lors['pl_area_per_child'] = lors['playground_area'] / lors['total_children']
#lors = lors.loc[lors['pl_area_per_child']!=lors['pl_area_per_child'].max()]

sns.relplot(lors, x='playground_count', y='poverty')
mpl.pyplot.show()