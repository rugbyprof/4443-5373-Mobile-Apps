(function (doc){
  window.SPRSettings = {
    'apiHost': "//productreviews.shopifycdn.com",
    'batchSize': 7,
  }

  var script = doc.createElement("script")
  script.type = "text/javascript";
  script.src = "https://productreviews.shopifycdn.com/assets/v4/spr-0e683603bfa450170bff33e7fbad64e7dfe9585e1caeb951bbe283e5a2306523.js";
  doc.getElementsByTagName("head")[0].appendChild(script);

  var link = doc.createElement("link")
  link.type = "text/css";
  link.rel = "stylesheet";
  link.media = "screen";
  link.href = "https://productreviews.shopifycdn.com/assets/v4/spr-07102fd76ff4bc22a3e0c32f0cca9ee51c77c34bbc4bdac79abb48f698de10dd.css";
  doc.getElementsByTagName("head")[0].appendChild(link);
})(document);
