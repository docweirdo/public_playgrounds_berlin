import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

playgrounds = pd.read_excel('../assets/playgrounds.xls', index_col='id', usecols=['id', 'anrechenbar Spielplatzversorgung', 'Nettospielfläche in m²', 'Größe in m² (Kataster)'])

# drop non accredible playgrounds, set total area for playable area for missing values
playgrounds = playgrounds[playgrounds['anrechenbar Spielplatzversorgung']].drop(['anrechenbar Spielplatzversorgung'], axis=1)
playgrounds['playground_area'] = playgrounds['Nettospielfläche in m²']
playgrounds['playground_area'] = playgrounds.apply(lambda row: row['Größe in m² (Kataster)'] if isinstance(row['playground_area'], str) else row['playground_area'], axis=1)
playgrounds.drop(['Größe in m² (Kataster)', 'Nettospielfläche in m²'], axis=1, inplace=True)
playgrounds.index.names = ['playground_id']

print(playgrounds[playgrounds['playground_area'] == playgrounds['playground_area'].max()])

ax = sns.displot(data=playgrounds, x="playground_area",  kind='hist', stat='percent')

ax.set(xlabel='Playarea of playground [m²]', ylabel='Fraction of playgrounds [%]')
plt.xlim(0, 7500)

fig = plt.gcf().get_figure()
fig.suptitle('Distribution of playarea across playgrounds')
fig.set_size_inches(12, 9)
fig.tight_layout()
plt.savefig("../figures/hist_playgrounds.svg", bbox_inches='tight')


plt.show()