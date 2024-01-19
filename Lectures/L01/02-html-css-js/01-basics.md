## Introduction to Web Development Basics

In this section: "Introduction to Web Development Basics", we'll focus on the foundational elements of web development: HTML, CSS, and basic JavaScript. 

### HTML Basics

HTML (HyperText Markup Language) is the standard markup language used to create web pages. It defines the structure of web content.

#### Sample HTML Code

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Web Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>Welcome to my first web page.</p>
</body>
</html>
```

- `<!DOCTYPE html>`: Declares the document type and HTML version.
- `<html>`: The root element of an HTML page.
- `<head>`: Contains meta-information about the document, like its title.
- `<title>`: Specifies the title of the document (shown in browser's title bar or tab).
- `<body>`: Contains the content of the document, such as text, images, links, etc.
- `<h1>`: Represents a header (largest header).
- `<p>`: Represents a paragraph.

### CSS Basics

CSS (Cascading Style Sheets) is used to style and layout web pages—for example, changing the color, font, and spacing of your content, splitting it into multiple columns, or adding animations and other decorative features.

#### Sample CSS Code

```css
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 20px;
    background-color: #f8f8f8;
}

h1 {
    color: navy;
}

p {
    color: #555;
}
```

- `body`, `h1`, `p` are selectors, which specify the HTML elements to style.
- Inside the curly braces `{ }`, there are properties and values. For example, `font-family: Arial, sans-serif;` sets the font style.

### JavaScript Basics

JavaScript is a scripting language used to create and control dynamic website content, like interactive forms, animations, etc.

#### Sample JavaScript Code

```html
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Example</title>
</head>
<body>
    <h1 id="header">Hello, World!</h1>
    <button onclick="changeText()">Click Me!</button>

    <script>
        function changeText() {
            document.getElementById("header").innerHTML = "Welcome to JavaScript!";
        }
    </script>
</body>
</html>
```

- The `<script>` tag contains JavaScript code.
- `function changeText() {...}` defines a function to change the text of the header.
- `document.getElementById("header").innerHTML = "Welcome to JavaScript!";` changes the content of the element with `id="header"`.

### Bringing It All Together

When teaching these concepts, it's important to show how they interact together. For example, you could start by explaining and demonstrating a basic HTML structure, then introduce CSS to style this HTML, and finally use JavaScript to add interactivity.

The provided examples are quite fundamental, but they offer a solid foundation for students to understand the essence of web development. You can then build upon these basics with more complex topics as the course progresses.