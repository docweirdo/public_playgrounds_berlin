from pyproj import Transformer;
import json

transformer = Transformer.from_crs("EPSG:25833", "EPSG:4326")

with open('../assets/playgrounds_wfs_rewound.geojson', encoding='utf-8') as f:
   playgrounds = json.load(f)


for f in playgrounds['features']:
    for i, c in enumerate(f['geometry']['coordinates'][0][0]):
        new_c = transformer.transform(c[0], c[1])
        f['geometry']['coordinates'][0][0][i] = [new_c[1], new_c[0]]

with open('../assets/playgrounds_wfs_rewound_transformed.geojson', mode='w+', encoding='utf-8') as f:
   json.dump(playgrounds, f, ensure_ascii=False)
