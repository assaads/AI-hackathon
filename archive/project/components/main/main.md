---
title: Main Component Guide
description: Documentation and usage guide for the Main component in the Starlight project.
---

# Main Component

The Main component is a part of the Starlight project's UI. It serves as a container that includes a navigation bar with links to different sections of the application or website. This component makes use of SCSS modules for styling and accepts an optional className for additional custom styling.

## Usage

To use the Main component in your project, you will need to import it and then include it in your JSX.

```
import { Main } from 'path_to_main_component';

// Later in your code, use the Main component
const App = () => {
    return (
        <main>
            <Main className="your-custom-classname" />
            {/* Other components */}
        </main>
    );
};
```

## Props

The Main component accepts the following props:

- `className`: An optional string that allows you to apply additional custom styles to the component by passing a CSS class name.

## Styling

The Main component uses SCSS modules for scoped styling. By default, the component's root element is styled with the class `.root` defined in the component's SCSS file (`main.module.scss`).

If you wish to override or extend the styles, you may pass an additional className to the Main component, which will then be applied in addition to the default styles.

### Example

```
<Main className="additional-class" />
```

In the above code snippet, the `additional-class` will be applied to the `div` element of the Main component, allowing you to extend or override the default styles as required.

## Navigation

The included navigation bar contains the following links by default:

- [Home](/home)
- [Projects](/projects)
- [About](/about)
- [Contact Us](/contact)

The navigation bar is just one part of the Main component intended to provide basic navigation around the application or website.

## Customization

To create custom component templates and modify the Main component further, you can refer to the documentation provided by Codux at [Codux custom component templates](https://help.codux.com/kb/en/article/kb16522).

## Best Practices

When customizing or extending the Main component, ensure that you follow best practices for accessibility and responsive design to maintain the quality and user-friendliness of the application or website.

## Conclusion

The Main component is a versatile and easily customizable part of the UI in the Starlight project. With the ability to pass a custom className and built-in navigation, the component serves as a starting point for developers to create a consistent look and feel across their application or website.