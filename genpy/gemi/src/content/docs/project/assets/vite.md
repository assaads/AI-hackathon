---
title: SVG Icon Integration Guide
description: Step-by-step instructions to embed and style SVG icons in your web project using the example SVG code.
---

# Importing an SVG Icon into an HTML File
This guide provides detailed instructions on how to include an SVG graphic (specifically, an icon) into your HTML web page. We will use an SVG icon with linear gradients as an example.

## Step 1: Understanding SVG Markup
Before we begin incorporating the SVG into a webpage, it's essential to understand its structure. An SVG (Scalable Vector Graphics) file is an XML-based vector image format for two-dimensional graphics that supports interactivity and animation.

The provided SVG markup contains several key components:

- XML namespace declarations (`xmlns` and `xmlns:xlink`) for SVG and XLink (for hyperlinking).
- `aria-hidden` and `role` attributes for accessibility, hiding the SVG from screen readers as it's being used for decoration.
- `class` attribute to apply CSS styles.
- `width` and `height` attributes to define the size of the SVG.
- `preserveAspectRatio` and `viewBox` attributes for scaling behavior and view position.

## Step 2: Embedding the SVG Code into HTML
To embed the provided SVG code into an HTML document, copy and paste the entirety of the `<svg>...</svg>` markup directly into the desired location within your HTML file's body.

```html
<body>
    <!-- Other HTML content -->
    
    <!-- SVG icon code starts here -->
    <svg xmlns="http://www.w3.org/2000/svg" ... > ... </svg>

    <!-- Other HTML content -->
</body>
```

## Step 3: Applying Styles
The SVG code specifies two linear gradients defined in the `<defs>` section. You can restyle these gradients or apply additional CSS to the SVG elements by referencing their classes or other attributes in your CSS file.

```css
.iconify--logos {
    /* Your custom styles */
}
```

### Customizing Gradients
You can modify the colors of the gradients by updating the `stop-color` values within the `<linearGradient>` elements.

## Step 4: Responsiveness and Accessibility
To ensure that the SVG scales properly on various devices, you can remove the `width` and `height` attributes and control the icon size using CSS. Keep the `preserveAspectRatio` and `viewBox` attributes.

For accessibility, even if the icon is for decoration and hidden from screen readers, it's still good practice to have a `<title>` or `<desc>` tag within the SVG with a description.

Example:
```html
<svg ...>
    <title>Decorative icon</title>
    <!-- SVG content -->
</svg>
```

## Additional Resources
Learn more about SVGs and how to use them in web development by visiting the following resources:
- [Scalable Vector Graphics (SVG)](https://developer.mozilla.org/en-US/docs/Web/SVG)
- [Using SVG](https://css-tricks.com/using-svg/)
- For a deeper understanding of how to document your code effectively, consider reading the [Diátaxis framework documentation](https://diataxis.fr/reference/).

Remember that a good guide helps the user to accomplish a specific task with clear and concise steps. Ensure your users understand the purpose of each step and avoid unnecessary jargon or complexity.