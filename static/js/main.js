// static/js/main.js

require([
    "esri/config",
     "esri/Map",
     "esri/views/MapView"
   ], function (esriConfig,Map, MapView) {

     esriConfig.apiKey = "AAPK773145a235ce4598814387d5c1aecab6zi4nkG2aAbnYt5M9XK4v3rEb6n6zA18k0KE6dcQEoD8Z74V2McXuo56561ZmHX7Q";
     const map = new Map({
       basemap: "arcgis-topographic" // Basemap layer
     });

     const view = new MapView({
       map: map,
       center: [-118.805, 34.027],
       zoom: 13, // scale: 72223.819286
       container: "viewDiv",
       constraints: {
         snapToZoom: false
       }
     });

   });