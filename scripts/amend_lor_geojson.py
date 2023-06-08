import json
import pandas as pd

lors = pd.read_csv(
    "../assets/lors_aggregated.csv", index_col="PLR_id", encoding="utf-8"
)

lors["pl_area_per_child"] = lors["playground_area"] / lors["total_children"]
lors['pl_area_per_child'] = lors['pl_area_per_child'].fillna(-1)


with open('../assets/lor_2021_rewound.geojson', encoding='utf-8') as f:
   lors_geo = json.load(f)


for i, f in enumerate(lors_geo['features']):
    props = f['properties']
    lors_geo['features'][i]['properties']['pl_area_per_child'] = lors.loc[int(props['PLR_ID'])]['pl_area_per_child']

with open('../assets/lors_2021_rewound_amended.geojson', mode='w+', encoding='utf-8') as f:
   json.dump(lors_geo, f, ensure_ascii=False)