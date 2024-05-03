---
title: Gemi-Doc How-To Guides
description: Detailed instructions for accomplishing specific tasks and utilizing advanced features within your Gemi-Doc project.
---

## Adding Custom CSS Styles

Gemi-Doc integrates Tailwind CSS for styling, but you can also include custom CSS styles to further personalize your documentation site. 

### Creating a Custom CSS File

1. **Create a CSS File:**
   Inside the `src/styles` directory (create it if it doesn't exist), create a new CSS file, such as `custom.css`.

2. **Add Custom Styles:** 
   In your CSS file, add your desired styles using standard CSS syntax. For example: 

```css 
/* src/styles/custom.css */
body {
  font-family: 'Arial', sans-serif; 
}

h1 {
  color: #333;
}
```

### Importing the CSS File

1. **Global Styles:**
   To apply the custom styles globally, import the CSS file into your `src/layouts/Layout.astro` file: 

```astro
---
import '../styles/custom.css';
---
```

2. **Page-Specific Styles:**
   For page-specific styles, import the CSS file directly into the desired Markdown or MDX file within the frontmatter:

```
---
import '../styles/custom.css'; 
title: My Page
---
```

## Using MDX for Advanced Content

Gemi-Doc supports MDX, which allows you to combine Markdown with JSX syntax. This enables you to embed interactive components and dynamic content within your documentation. 

### Example: Embedding a React Component

1. **Create a React Component:**
   Define a React component in a separate file within your `src/components` directory (create it if needed). For instance: 

```jsx 
// src/components/MyComponent.jsx
function MyComponent() {
  return <div>This is my React component!</div>;
}

export default MyComponent; 
```

2. **Import and Use in MDX:**
   In your MDX file, import the React component and use it within the content:

```mdx
---
title: Using Components 
---

import MyComponent from '../../components/MyComponent'; 

Here's an example of using a React component: 

<MyComponent /> 
```

This will render the React component within your MDX page, allowing you to create interactive and dynamic documentation experiences. 
