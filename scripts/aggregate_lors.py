import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# change datatype for area_sqm
lors['area_sqm'] = lors['area_sqm'].str.replace(',', '.').astype(float)

# aggregate children
population['total_children'] = population['<6'] + population['6-15'] + population['15-18']

lors_playgrounds = lors_playgrounds.join(playgrounds, on='playground_id')

# count playgrounds within Lor
agg_funcs = {'playground_id': 'count', 'playground_area': 'sum'}
lors[['playground_count', 'playground_area']] = lors_playgrounds[['playground_id', 'playground_area']].groupby('PLR_id').aggregate(agg_funcs)

# if no association could be made, row is NaN, fill with 0 playgrounds respective area
lors['playground_count'].fillna(0, inplace=True)
lors['playground_area'].fillna(0, inplace=True)

childpoverty = childpoverty.join(population[['total_population', 'total_children', '<6', '6-15', '15-18']])
# childpoverty['poor_children'] = childpoverty['total_children'] * childpoverty['poverty'] / 100

lors = lors.join(childpoverty)

# lors.to_csv('../assets/lors_aggregated.csv', encoding='utf-8')
# exit()

# Scatterplot ages
# plot = pd.DataFrame([])
# plot2 = pd.DataFrame([])
# plot3 = pd.DataFrame([])

# plot['pl_area_per_child'] = lors['playground_area'] / lors['<6']
# plot['age'] = 'Age <5'
# plot2['pl_area_per_child'] = lors['playground_area'] / lors['6-15']
# plot2['age'] = 'Age 6-15'
# plot3['pl_area_per_child'] = lors['playground_area'] / lors['15-18']
# plot3['age'] = 'Age 15-18'

# plot = pd.concat([plot, plot2], axis=0)
# plot = pd.concat([plot, plot3], axis=0)
# plot['poverty'] = childpoverty['poverty']

# ax = sns.lmplot(plot, x='pl_area_per_child', y='poverty', hue='age', legend=False)
# ax.set(xlabel='Playarea per child [m²]', ylabel='Child poverty [%]')

# plt.legend(loc='upper right', title="Agegroup in PLR")

# plt.ylim(0, None)
# plt.xlim(0, 150)

# fig = plt.gcf().get_figure()
# fig.suptitle('Playarea per child by age against child poverty in each PLR')
# fig.set_size_inches(12, 9)
# fig.tight_layout()
# plt.savefig("../figures/scatter_poverty_pl_area_age.svg", bbox_inches='tight')


# Scatterplot total
# lors['pl_area_per_child'] = lors['playground_area'] / lors['total_children']
# ax = sns.lmplot(lors, x='pl_area_per_child', y='poverty')
# ax.set(xlabel='Playarea per child [m²]', ylabel='Child poverty [%]')

# plt.ylim(0, None)
# plt.xlim(0, None)

# fig = plt.gcf().get_figure()
# fig.suptitle('Playarea per child against child poverty in each PLR')
# fig.set_size_inches(12, 9)
# fig.tight_layout()
# plt.savefig("../figures/scatter_poverty_pl_area.svg", bbox_inches='tight')

# print(lors)
# exit()

# Boxplot 
lors['pl_area_per_child'] = lors['playground_area'] / lors['total_children']
ax = sns.boxplot(lors, x='pl_area_per_child')

ax.set(xlabel='Playarea per child [m²]')

fig = plt.gcf().get_figure()
fig.suptitle('Distribution of playarea per child across all PLRs')
fig.set_size_inches(12, 9)
fig.tight_layout()
plt.savefig("../figures/box_pl_area.svg", bbox_inches='tight')

# print(lors)
# exit()


plt.show()