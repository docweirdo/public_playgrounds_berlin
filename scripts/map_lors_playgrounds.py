import pandas as pd
import shapely
from shapely.geometry import shape
import json

with open('../assets/playgrounds_wfs_rewound_transformed.geojson', encoding='utf-8') as f:
    playgrounds = json.load(f)

with open('../assets/lor_2021_rewound.geojson', encoding='utf-8') as f:
    lors = json.load(f)

df_lors_playgrounds = pd.DataFrame(columns=['PLR_id', 'playground_id'])

lor_shape = shape(lors['features'][0]['geometry'])


# convert geometry geojson to shape
for i, f in enumerate(lors['features']):
    lor_shape = shape(f['geometry'])
    intersecting_playgrounds = []

    # if not shapely.is_valid(lor_shape):
    #     print(shapely.is_valid_reason(lor_shape))

    for k, p in enumerate(playgrounds['features']):
        if p['properties']['anrech_sp'] == 'Nein':
            continue
        
        playground_shape = shape(p['geometry'])

        # if not shapely.is_valid(playground_shape):
        #     print(shapely.is_valid_reason(playground_shape))

        if lor_shape.intersects(playground_shape):
            intersecting_playgrounds.append({'PLR_id': f['properties']['PLR_ID'], 'playground_id': p['id']})

    df_extended = pd.DataFrame(intersecting_playgrounds, columns=df_lors_playgrounds.columns)       
    df_lors_playgrounds = pd.concat([df_lors_playgrounds, df_extended])
    
df_lors_playgrounds.to_csv('../assets/lor_playgrounds.csv', encoding='utf-8', mode='w+', index=False)