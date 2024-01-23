
    (function() {
      var baseURL = "https://cdn.shopify.com/shopifycloud/checkout-web/assets/";
      var scripts = ["https://cdn.shopify.com/shopifycloud/checkout-web/assets/runtime.latest.en.139fbd3f8b22dd679c81.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/334.latest.en.542825689c18403c43d5.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/283.latest.en.93337359cb8d3a49b3f0.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/150.latest.en.ddc10927ad5c786fc8fb.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/app.latest.en.e29c247677fbd27788f5.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/731.latest.en.13d4de92b88330e8fea9.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/958.latest.en.0a32e65bbeeffe7bac95.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/844.latest.en.7fcd45ae446a9a5574e8.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/OnePage.latest.en.18afedce9ccde2c32fe3.js"];
      var styles = ["https://cdn.shopify.com/shopifycloud/checkout-web/assets/334.latest.en.0b463e113780a7092e3c.css","https://cdn.shopify.com/shopifycloud/checkout-web/assets/app.latest.en.e5a7f63ca146c0549466.css","https://cdn.shopify.com/shopifycloud/checkout-web/assets/958.latest.en.3388a58cacfe5a93e981.css","https://cdn.shopify.com/shopifycloud/checkout-web/assets/74.latest.en.d207b26f9fce16be7891.css"];
      var fontPreconnectUrls = ["https://fonts.shopifycdn.com"];
      var fontPrefetchUrls = ["https://fonts.shopifycdn.com/lato/lato_n4.c86cddcf8b15d564761aaa71b6201ea326f3648b.woff2?h1=Y2FuZHlzdG9yZS5jb20&hmac=ea5d1adeb756664c1ac3aa21d57044466173be7d451e4d7ab468386f7eb15ae3","https://fonts.shopifycdn.com/lato/lato_n7.f0037142450bd729bdf6ba826f5fdcd80f2787ba.woff2?h1=Y2FuZHlzdG9yZS5jb20&hmac=f6362b621bde0a57d9228b58db2d67fc066ecf6ea3f85a94c5bf0e029a72b9b0"];
      var imgPrefetchUrls = ["https://cdn.shopify.com/s/files/1/0614/8309/0107/files/checkout-logo-007_x320.png?v=1649177477"];

      function preconnect(url, callback) {
        var link = document.createElement('link');
        link.rel = 'dns-prefetch preconnect';
        link.href = url;
        link.crossOrigin = '';
        link.onload = link.onerror = callback;
        document.head.appendChild(link);
      }

      function preconnectAssets() {
        var resources = [baseURL].concat(fontPreconnectUrls);
        var index = 0;
        (function next() {
          var res = resources[index++];
          if (res) preconnect(res[0], next);
        })();
      }

      function prefetch(url, as, callback) {
        var link = document.createElement('link');
        if (link.relList.supports('prefetch')) {
          link.rel = 'prefetch';
          link.fetchPriority = 'low';
          link.as = as;
          if (as === 'font') link.type = 'font/woff2';
          link.href = url;
          link.crossOrigin = '';
          link.onload = link.onerror = callback;
          document.head.appendChild(link);
        } else {
          var xhr = new XMLHttpRequest();
          xhr.open('GET', url, true);
          xhr.onloadend = callback;
          xhr.send();
        }
      }

      function prefetchAssets() {
        var resources = [].concat(
          scripts.map(function(url) { return [url, 'script']; }),
          styles.map(function(url) { return [url, 'style']; }),
          fontPrefetchUrls.map(function(url) { return [url, 'font']; }),
          imgPrefetchUrls.map(function(url) { return [url, 'image']; })
        );
        var index = 0;
        (function next() {
          var res = resources[index++];
          if (res) prefetch(res[0], res[1], next);
        })();
      }

      function onLoaded() {
        preconnectAssets();
        prefetchAssets();
      }

      if (document.readyState === 'complete') {
        onLoaded();
      } else {
        addEventListener('load', onLoaded);
      }
    })();
  