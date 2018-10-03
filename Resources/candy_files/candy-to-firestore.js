const admin = require('./node_modules/firebase-admin');
const serviceAccount = require("./service-key.json");

var data = require("./candy_5.json");


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
                .collection("candy")
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
