---
title: Setting Up React with Semantic UI
description: A step-by-step guide to initializing a React application with Semantic UI integration.
---

# Introduction
In this guide, we will walk you through the process of creating a root element for a React application and integrating Semantic UI for styling. Follow these instructions to set up your project for development with a sleek user interface.

# Prerequisites
Before you begin, ensure you have the following installed:
- [Node.js](https://nodejs.org/)
- [npm](https://www.npmjs.com/) (usually comes with Node.js)
- A code editor (like [Visual Studio Code](https://code.visualstudio.com/))

# Step 1: Create React App
Start by creating a new React application if you haven't already. You can use the `create-react-app` command for a quick setup.

```
npx create-react-app my-app
cd my-app
```

# Step 2: Install Semantic UI CSS
Semantic UI is a development framework that helps create beautiful, responsive layouts using human-friendly HTML. To add Semantic UI to your React project, you need the CSS file. Install it with npm:

```
npm install semantic-ui-css
```

# Step 3: Import Semantic UI CSS
After installing Semantic UI, import the CSS file into your project's entry file (usually `index.js` or `index.tsx`) to use the framework's styles throughout your app.

```javascript
import 'semantic-ui-css/semantic.min.css';
```

# Step 4: Set Up React Root
React 18 introduced a new root API. Use `ReactDOM.createRoot` to create a root for your application.

```javascript
const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
```

Ensure you have a div with the id 'root' in your `public/index.html` file where the React application will mount.

# Step 5: Enable Strict Mode
React's StrictMode is a helpful tool for highlighting potential problems in an application. It activates additional checks and warnings for its descendants.

In your entry file, wrap your `<App />` component with `<React.StrictMode>` to enable it.

```javascript
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
```

# Conclusion
You have now successfully set up your React application with Semantic UI. Your project is ready for you to build out your components with the assurance that you have a solid and stylish CSS framework at your disposal.

For more details on Semantic UI and its components, visit the official [Semantic UI documentation](https://react.semantic-ui.com/). To learn more about React's strict mode and root API, you can refer to the [React documentation](https://reactjs.org/docs/strict-mode.html).