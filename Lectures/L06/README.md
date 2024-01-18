## Example Javascript Html Css 

To create a basic example of using vanilla JavaScript, HTML, and CSS to interact with server-side data, let's consider a scenario where we have a simple web page with a button and a div element. When the button is clicked, it triggers a JavaScript function that makes an AJAX request to fetch tabular data (like the one you provided) from a server-side source. This data is then displayed in the div element.

Here's a breakdown of the steps involved:

1. **HTML**: Create a basic HTML structure with a button and a div element.
2. **CSS**: Add some basic styling to make it visually appealing.
3. **JavaScript**: Write a JavaScript function to handle the button click event. This function will make an AJAX request to a server-side endpoint (which you'll need to implement) that returns the tabular data in JSON format. Once the data is fetched, it will be formatted as an HTML table and displayed in the div element.

Let's start with the HTML structure:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Data Fetch Example</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <button id="loadDataButton">Load Data</button>
    <div id="dataContainer"></div>
    <script src="script.js"></script>
</body>
</html>
```

For the CSS (style.css):

```css
#loadDataButton {
    margin: 10px;
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
}

#dataContainer {
    margin: 10px;
    padding: 10px;
    border: 1px solid #ddd;
}
```

And for the JavaScript (script.js):

```javascript
document.getElementById('loadDataButton').addEventListener('click', function() {
    fetch('https://your-server.com/api/data')
        .then(response => response.json())
        .then(data => {
            const table = createTable(data);
            document.getElementById('dataContainer').innerHTML = table;
        })
        .catch(error => console.error('Error:', error));
});

function createTable(data) {
    let table = '<table border="1"><tr>';
    for (let key in data[0]) {
        table += `<th>${key}</th>`;
    }
    table += '</tr>';

    data.forEach(row => {
        table += '<tr>';
        for (let key in row) {
            table += `<td>${row[key]}</td>`;
        }
        table += '</tr>';
    });

    table += '</table>';
    return table;
}
```

In the JavaScript code, replace `'https://your-server.com/api/data'` with the actual URL of your server-side endpoint that returns the JSON data. The `createTable` function dynamically creates an HTML table based on the JSON data.

Remember, you'll need a server-side script (like a Node.js/Express or a PHP script) that serves the data in JSON format at the specified endpoint. This is just a client-side example, and server-side implementation depends on your backend technology.