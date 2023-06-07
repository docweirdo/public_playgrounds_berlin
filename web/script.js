

var map = L.map('map').setView([52.520008, 13.404954], 10);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

let fetch_LORs = async () => {

    let response = await fetch('../assets/lor_2021_rewound.geojson')
        .then(res => res.text());
    
    let LORs = JSON.parse(response);

    response = await fetch('../assets/playgrounds_wfs_rewound_transformed.geojson')
    .then(res => res.text());

    let playgrounds = JSON.parse(response);

    let [min, max] = get_max_min(LORs);

    console.log(min,max)

    L.geoJSON(LORs, {
        style: function(feature) {
            return {
                fillColor: get_color(feature.properties.GROESSE_M2, min, max),
                weight: 2,
                opacity: 1,
                color: 'black',
                dashArray: '3',
                fillOpacity: 0.3
            };
        }
    }).addTo(map);

    console.log(playgrounds)
    L.geoJSON(playgrounds).addTo(map);

}

function get_color(size, min, max) {
    let grade = (max - min)/6;

    return  size > 5*grade ? '#bd0026' :
    size > 4*grade  ? '#f03b20' :
    size > 3*grade  ? '#fd8d3c' :
    size > 2*grade   ? '#feb24c' :
    size > grade   ? '#FED976' :
               '#ffffb2';

}

function get_max_min(geoJSON) {

    let min = geoJSON.features[0].properties.GROESSE_M2;
    let max = geoJSON.features[0].properties.GROESSE_M2;

    for (feature of geoJSON.features) {

        let val = feature.properties.GROESSE_M2;

        if (val > max) {
            max = val;
        } else if (val < min) {
            min = val
        }
    
        if (feature.properties.PLR_ID === '01100416'){
            console.log(feature.properties.PLR_ID)
            console.log(get_color(feature.properties.GROESSE_M2, 133642.042, 23734915.62))
        }
    }

    return [min, max]
}

fetch_LORs();
