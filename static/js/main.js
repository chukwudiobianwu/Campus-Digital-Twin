// static/js/main.js

require([
    "esri/config",
    /** 
     "esri/Map",
     "esri/views/MapView"
     */
     "esri/WebScene",
     "esri/views/SceneView",
     "esri/widgets/Legend"
   ], function(esriConfig, WebScene, SceneView, Legend) {

     esriConfig.apiKey = "AAPK773145a235ce4598814387d5c1aecab6zi4nkG2aAbnYt5M9XK4v3rEb6n6zA18k0KE6dcQEoD8Z74V2McXuo56561ZmHX7Q";
     /** 
     const map = new Map({
       basemap: "arcgis-topographic" // Basemap layer
     });

     const view = new MapView({
       map: map,
       center: [-123.3117, 48.4647],
       zoom: 13, // scale: 72223.819286
       container: "viewDiv",
       constraints: {
         snapToZoom: false
       }
     });
     
   var sceneLayer = new SceneLayer({
    url: "https://uvgeog.maps.arcgis.com/home/item.html?id=bdee0d4108a147a0b9719d04f1ec699f"
  });
  map.add(sceneLayer);
  */
  const webscene = new WebScene({
    portalItem: {
      id: "bdee0d4108a147a0b9719d04f1ec699f"
    }
  });
 
  const view = new SceneView({
    container: "viewDiv",
    map: webscene
  });

  const legend = new Legend ({
    view:view
  });

  view.ui.add(legend, "top-right");

   }); 

