---
title: SVG Module Declaration Guide
description: Learn how to handle SVG imports in your TypeScript project with React.
---

# SVG Module Declaration in TypeScript

When working with a TypeScript project that incorporates SVG files, especially within a React framework, you might want to import SVGs directly as React components. This guide walks you through declaring a module for SVG imports, enabling seamless use of SVGs as React components in your project.

## Understanding the Module Declaration

Before modifying your TypeScript declarations, it's important to understand what each part of the code means and how it contributes to your ability to use SVG files as React components.

### The `declare module '*.svg'` Syntax

At the heart of this feature is the module declaration syntax:

```typescript
declare module '*.svg' {
    //... module contents ...
}
```

This tells TypeScript that any file ending with `.svg` should be treated as a module, and here's what is defined within this module.

## Importing React

The first line inside the module declaration imports React since we are going to use SVGs as React components.

```typescript
import * as React from 'react';
```

This brings all the exports from React into the scope of our module declaration.

### The `ReactComponent` Export

Inside the module, a constant named `ReactComponent` is exported. This is a React functional component tailored for SVG elements.

```typescript
export const ReactComponent: React.FunctionComponent<React.ComponentProps<'svg'> & { title?: string }>;
```

- `React.FunctionComponent<React.ComponentProps<'svg'>>`: Defines a standard React functional component with properties (`props`) that correspond to a regular SVG element's props.
- `{ title?: string }`: An additional optional `title` prop is included to provide a title for the SVG, which is useful for accessibility purposes.

## Default Export

Finally, the module defines a default export:

```typescript
export default ReactComponent;
```

This default export makes it easy to import the SVG as a component without needing to reference a named export explicitly.

## Integrating the SVG Module Declaration

1. Copy the provided module declaration code into a `.d.ts` file in your project (e.g., `svg.d.ts`).
2. Ensure the declaration file is included in your TypeScript project by referencing it in your `tsconfig.json` under the "include" array.
3. Now, when you import an SVG file into your React components, it will be treated as a ReactComponent, allowing you to use it like this:

```jsx
import { ReactComponent as Logo } from './logo.svg';

const App = () => (
  <div>
    <h1>My Project</h1>
    <Logo title="Project Logo" />
  </div>
);
```

The SVG is now a part of your component hierarchy, with all the power of React's composability and props system.

## Conclusion

By declaring an SVG module, you gain a powerful way to use SVG files as components in your React and TypeScript project. This simplifies working with SVGs, keeps your code clean and maintainable, and leverages TypeScript's strong typing to enhance your development workflow.

For more information on module declaration patterns and TypeScript with React, you might find these resources helpful:
- [TypeScript Module Documentation](https://www.typescriptlang.org/docs/handbook/modules.html)
- [React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app/)

Remember, the power of TypeScript lies in its flexibility and integration capabilities. With this guide, you're now equipped to create more descriptive and accessible UIs with SVGs in your TypeScript React projects.