

var map = L.map('map').setView([52.520008, 13.404954], 10);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


let fetch_LORs = async () => {

    let geojson = await fetch('assets/rewound-geojson.json')
        .then(res => res.text());
    
    let geojsonObject = JSON.parse(geojson);

    console.log(geojsonObject);

    L.geoJSON(geojsonObject).addTo(map);

}

fetch_LORs();
