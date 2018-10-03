const admin = require('./node_modules/firebase-admin');
const serviceAccount = require("./service-key.json");

var data = [
	{"id":"0","type":"individually-wrapped"},
	{"id":"1","type":"unwrapped-loose"},
	{"id":"2","type":"gummy"},
	{"id":"3","type":"old-fashioned"},
	{"id":"4","type":"chocolate"},
	{"id":"5","type":"salt-water-taffy"},
	{"id":"6","type":"lollipops-suckers"},
	{"id":"7","type":"hard-candy"},
	{"id":"8","type":"bagged-candy"},
	{"id":"9","type":"candy-bars"},
	{"id":"10","type":"caramel"},
	{"id":"11","type":"cinnamon-red-hot"},
	{"id":"12","type":"coated"},
	{"id":"13","type":"foil-wrapped"},
	{"id":"14","type":"gum-bubblegum"},
	{"id":"15","type":"jawbreakers"},
	{"id":"16","type":"jelly-beans"},
	{"id":"17","type":"jewelry-edible"},
	{"id":"18","type":"kosher"},
	{"id":"19","type":"licorice"},
	{"id":"20","type":"liquid-gel"},
	{"id":"21","type":"marshmallow"},
	{"id":"22","type":"mini-sized"},
	{"id":"23","type":"mints"},
	{"id":"24","type":"novelty"},
	{"id":"25","type":"nuts"},
	{"id":"26","type":"powder"},
	{"id":"27","type":"retro"},
	{"id":"28","type":"rock-candy"},
	{"id":"29","type":"scoops-containers-displays"},
	{"id":"30","type":"soft"},
	{"id":"31","type":"sour"},
	{"id":"32","type":"sports-candy"},
	{"id":"33","type":"sugar-free"},
	{"id":"34","type":"theater-king-size"}
];
//"foil-wrapped","marshmallow","mini-sized"

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: "https://msu-candy-store.firebaseio.com"
});

data && Object.keys(data).forEach(key => {
    const nestedContent = data[key];

    if (typeof nestedContent === "object") {

        console.log(key);
        console.log(data[key]);
        
        Object.keys(nestedContent).forEach(docTitle => {
            
            admin.firestore()
                .collection("candy_types")
                .doc(key)
                .set(data[key])
                .then((res) => {
                    console.log("Document successfully written!");
                })
                .catch((error) => {
                    console.error("Error writing document: ", error);
                });
        });
    }
});
