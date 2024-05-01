---
title: CSS Structure Guide
description: A guide to understanding the basic structure of a CSS code block for styling webpages.
---

# Introduction to CSS Syntax
This guide will walk you through the basic syntax of Cascading Style Sheets (CSS), the language used for describing the presentation of a document written in HTML or XML. Understanding this syntax is key to styling your webpages effectively.

# CSS Syntax Overview
CSS is made up of `selectors` and `declaration blocks`. The `.root` syntax provided is an example of a class selector, which can be used to style elements that have a specific class attribute.

## Selectors
Selectors are patterns that define which elements within the Document Object Model (DOM) to target and style. There are various types of selectors in CSS, and `.root` is a class selector example, which targets any element that has a class attribute with the value `root`.

### .root Selector
Here is the provided code block:

```css
.root {
}
```
The `.root` is a class selector, indicated by the period `.` preceding the word `root`. It selects all elements that have a class of `root`. Inside the braces `{}` would be the declarations to style the selected elements.

# Writing CSS Declarations
A declaration block contains one or more declarations separated by semicolons. Each declaration includes a CSS property name and a value, separated by a colon. 

## Example of a Declaration Block
Here's what a simple declaration block could look like when applied to the `.root` selector:

```css
.root {
    color: #333;
    background-color: #f8f8f8;
    padding: 10px;
    margin: 0 auto;
}
```

- `color` defines the text color.
- `background-color` specifies the background color of the element.
- `padding` sets the space between the content of the element and its border.
- `margin` defines the space outside the border.

# Applying CSS to HTML
To apply your CSS styles to an HTML document, you must link the CSS file using the `<link>` tag in the head section of your HTML file or include the styles within a `<style>` tag.

## Linking External CSS
Here is an example of linking an external CSS file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="root">Content goes here</div>
</body>
</html>
```
Remember, the `href` attribute should contain the path to your CSS file.

Guides lead a user through a specific task they want to accomplish, often with a sequence of steps. Writing a good guide requires thinking about what your users are trying to do.

For further reading and reference, check out the comprehensive guide on CSS at [MDN Web Docs - CSS](https://developer.mozilla.org/en-US/docs/Web/CSS).


