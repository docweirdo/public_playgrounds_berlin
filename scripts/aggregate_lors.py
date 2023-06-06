import pandas as pd

lors = pd.read_csv('../assets/lor_2021.csv', sep=';', index_col='PLR_id')
children = pd.read_csv('../assets/children_06_2022.csv', sep=',', index_col='PLR')

lors = lors.join(children)

print(lors)