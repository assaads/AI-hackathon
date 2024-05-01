---
title: NewComponent Usage Guide
description: A comprehensive guide on how to use the NewComponent in your React projects.
---

# Introduction to NewComponent
The `NewComponent` is a React component designed to be easily integrated into your application. It comes styled with SCSS modules and accepts a `className` prop for additional customization. This guide will lead you through the process of using the `NewComponent` in your project and how to customize it to fit your needs.

# Including NewComponent in Your Project

## Importing the Necessary Modules
To start using `NewComponent`, you need to import it along with its styles into your React component file:

```javascript
import { NewComponent } from 'path/to/NewComponent';
import styles from 'path/to/new-component.module.scss';
```

Ensure you have the correct path to where the `NewComponent` file is located within your project.

## Using NewComponent in JSX
Once imported, you can use `NewComponent` within your JSX as follows:

```jsx
<NewComponent className="my-custom-class" />
```

- `className`: A string that allows you to provide additional CSS classes to the component for customization purposes.

# Customizing NewComponent

## Overriding Styles with className
You can pass a custom class to the component to override its default styles:

```jsx
<NewComponent className="my-custom-class" />
```

In your CSS or SCSS file, define `.my-custom-class` with your desired styles:

```scss
.my-custom-class {
  /* Custom styles here */
}
```

## Using SCSS Modules
`NewComponent` is styled using SCSS modules, which encapsulate styles locally to avoid clashes with other styles in your application. You can directly modify the `new-component.module.scss` file to change the component's appearance:

```scss
.root {
  /* Modify default styles here */
}
```

# Conclusion

`NewComponent` provides a simple and customizable component template for your React applications. By following the steps in this guide and utilizing CSS or SCSS for styling, you can easily integrate and adapt the `NewComponent` to fit the look and feel of your project.

For more information on creating custom component templates, visit [Codux's Custom Component Templates](https://help.codux.com/kb/en/article/kb16522).

For more detailed information about writing documentation, you might want to check out [about reference](https://diataxis.fr/reference/).