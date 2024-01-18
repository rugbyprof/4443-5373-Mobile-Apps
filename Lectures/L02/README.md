## HTML and CSS Basics

HTML (HyperText Markup Language) and CSS (Cascading Style Sheets) are the foundational technologies for building web pages. HTML provides the structure of the page, while CSS defines its style.

### HTML Basics

HTML documents are structured as a collection of nested elements, each represented by tags.

**Sample HTML Code:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Sample Web Page</title>
</head>
<body>
    <h1>Welcome to My Web Page</h1>
    <p>This is a paragraph on my web page.</p>
    <a href="https://example.com">Click here to visit Example.com</a>
</body>
</html>
```

- `<!DOCTYPE html>`: Declares the document type and version of HTML.
- `<html>`: The root element of an HTML document.
- `<head>`: Contains meta-information about the document.
- `<title>`: Specifies the title of the document.
- `<body>`: Contains the content of the document.
- `<h1>`: Defines a top-level heading.
- `<p>`: Defines a paragraph.
- `<a>`: Defines a hyperlink.

#### CSS Basics

CSS is used to control the presentation of HTML documents. It allows for separating the content structure from the design aspects.

**Sample CSS Code:**

```css
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

h1 {
    color: darkblue;
}

p {
    color: gray;
}

a {
    color: teal;
    text-decoration: none;
}
```

- The `body` selector styles the entire body of the HTML document.
- `font-family`, `line-height`, `margin`, and `padding` are properties that define the font, line spacing, and spacing around elements.
- `h1`, `p`, `a` selectors target the respective HTML elements.
- `color` and `text-decoration` properties define the text color and link decoration.

### Integrating HTML with CSS

CSS can be integrated into an HTML document either internally using a `<style>` tag in the `<head>` section, linked externally from a separate `.css` file, or in-line directly within HTML elements.

**Sample Integration of HTML and CSS:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Sample Web Page with CSS</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        h1 {
            color: darkblue;
        }
        p {
            color: gray;
        }
        a {
            color: teal;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Styled Web Page</h1>
    <p>This is a styled paragraph.</p>
    <a href="https://example.com">Visit Example.com</a>
</body>
</html>
```

In this example, the CSS is placed within a `<style>` tag in the document's head. This is an effective way to apply styles to a single HTML document. For larger projects, external CSS files are generally preferred for better organization and reusability.