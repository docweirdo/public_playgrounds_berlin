

var map = L.map('map').setView([52.520008, 13.404954], 10);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

let fetch_LORs = async () => {

    let response = await fetch('https://dl.dropbox.com/s/6cbejuci59llu70/lors_2021_rewound_amended.geojson?dl=1')
        .then(res => res.text());
    
    let LORs = JSON.parse(response);

    response = await fetch('https://dl.dropbox.com/s/31qo9aa4g1yi5yj/playgrounds_wfs_rewound_transformed.geojson?dl=1')
    .then(res => res.text());

    let playgrounds = JSON.parse(response);

    L.geoJSON(LORs, {
        style: function(feature) {
            return {
                fillColor: get_color(feature.properties.pl_area_per_child),
                weight: 2,
                opacity: 1,
                color: 'black',
                dashArray: '3',
                fillOpacity: 0.6
            };
        }
    }).addTo(map);

    L.geoJSON(playgrounds).addTo(map);

}

function get_color(value) {

    if (value>6.24) return '#ffffb2'
    else if (value>4.14) return '#FED976'
    else if (value>2.85) return '#feb24c'
    else if (value>1.55) return '#fd8d3c'
    else if (value>0) return '#f03b20'
    else return '#808080'
    

}


fetch_LORs();
