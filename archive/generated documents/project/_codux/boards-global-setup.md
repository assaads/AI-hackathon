---
title: Importing Semantic UI CSS in Your Project
description: Step-by-step instructions for including Semantic UI in your web project to enhance its style and functionality.
---

# Introduction
This guide will walk you through the process of importing Semantic UI's minified CSS file into your web project. Semantic UI is a development framework that helps create responsive, elegant, and readable HTML layouts with ease.

## What is Semantic UI?
Semantic UI is a UI component framework that provides pre-designed widgets and styling conventions for building beautiful websites. It uses human-friendly HTML syntax, making your development process more intuitive.

## Prerequisites
Before you start, make sure you have:

- A basic understanding of HTML and CSS
- A project where you can include the Semantic UI CSS file
- Node.js and npm installed on your system (if you plan to install Semantic UI via npm)

# How to Import Semantic UI CSS
Incorporating the Semantic UI CSS style definitions into your project involves a few simple steps.

## Method 1: Direct Import
The most straightforward way to use Semantic UI CSS is by importing the minified version directly in your HTML file.

### Step 1: Locate the CSS File
Find the `semantic.min.css` file within the `semantic-ui-css` package.

### Step 2: Include in HTML
Add the following line to the `<head>` section of your HTML document:
```html
<link rel="stylesheet" type="text/css" href="path/to/semantic-ui-css/semantic.min.css">
```
Replace `path/to/` with the actual path to the `semantic.min.css` file in your project structure.

## Method 2: Using npm
Alternatively, you can manage your project's dependencies through npm.

### Step 1: Install Semantic UI CSS Package
Run the following command in your project's root directory:
```shell
npm install semantic-ui-css
```

### Step 2: Import in Your JavaScript Module
In the JavaScript file where you want to include Semantic UI styles, add the import statement at the top:
```javascript
import 'semantic-ui-css/semantic.min.css';
```

This line tells your module bundler to include the Semantic UI styles in your build.

# Conclusion
By following the steps above, you have successfully added Semantic UI CSS to your web project. This will give you access to a vast array of styled components and layouts that are ready to use in your application.

- Ensure that you understand the thematic conventions Semantic UI uses so that you can use its components effectively.
- For more advanced topics, such as customizing themes, refer to the official Semantic UI documentation.

For a deeper understanding of Semantic UI, its components, and customization, visit the [official Semantic UI documentation](https://semantic-ui.com/introduction/getting-started.html).

Remember, writing guides is all about helping your users accomplish tasks smoothly. Always focus on clarity, sequence, and practical tips that address common pain points.