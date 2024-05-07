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

     esriConfig.apiKey = "AAPKd2efe1158aaa4ecca1064e0cc644fc734prfKOIG382Y1tqSyvcXps72_xfo9dHaQbuDDox8HGqKiXlAR5nwU6O2JdZtGT-f";
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
      id: "5c2b9ac61b754c7e8ec967f826129472"
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

  view.on("click", function(event) {
    // Perform a hitTest to identify 3D objects clicked on
    view.hitTest(event).then(function(response) {
        // Check if any objects were identified
        if (response.results.length > 0) {
            // Get the attributes of the first identified object
            const attributes = response.results[0].graphic.attributes;
            // Access the attribute containing the name of the building
            const buildingName = attributes["name"]; // Adjust the attribute name accordingly
            // Display the name of the building
            document.getElementById("buildingName").value = buildingName; 
        }
    });
});

fetch('/get_issues')
  .then(response => response.json())
  .then(data => {
    console.log(data.message);  // Log message to browser console
    console.log(data.issues);   // Log issues to browser console
  })
  .catch(error => console.error('Error:', error));
   }); 

