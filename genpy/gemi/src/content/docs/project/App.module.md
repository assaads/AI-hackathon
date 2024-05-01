---
title: CSS Style Guide for Web Components
description: An in-depth description and guide for styling web components in a modern webpage.
---

# CSS Style Guide for Web Components
This guide provides documentation on a collection of CSS classes that have been created to style and layout web components within a webpage. Understanding these classes will aid in the design and development of an aesthetically pleasing and functional website.

## Page Layout and Structure

### .page
- Configures the general layout of the page using CSS Grid.
- Distributes space evenly between three columns.
- Centralizes the page with automatic margins.
- Set to a fixed width of 1024 pixels with padding.
- Allows overflow content to scroll within the grid items.
- Centers content within the grid cells.

### .labels and .actions
- Both classes utilize the Flexbox layout for inline or block elements.
- `.labels` places items evenly spaced from end to end of the container.
- `.actions` holds its items in a row with a small gap and a slight top padding.

### .two-columns
- Allows for a flexible layout of two columns optimized for content alignment and spacing.
- Adjusts the last item to have even distribution and top padding for visual balance.

## Typography and Fonts

### .title
- Adorns text with the FUTURA font.
- Applies normal font weight and large font size for impactful headings.
- Adjusts letter spacing for a tighter look and manages line height for readability.

### .description
- Utilizes FUTURA font in a smaller size for subtler descriptive text.

## Images, Buttons, and Forms

### .profile-img
- Controls the size of profile images for consistency within the layout.

### .button-showcase and .buttons-row
- Organizes buttons vertically with `.button-showcase`, including a separation gap.
- `.buttons-row` aligns buttons in a row, with varying gaps and margin setups at the last item to distinguish between sections.

### .name-input
- Styles a flex container aimed at form input fields aligned with their labels.
- Manages width and spacing for the input and accompanying label or span element.

## Additional Component Layouts

### .wireframes
- Uses Flexbox to distribute children elements with equal space around them.

### .social-showcase and .icons
- Constructs a columnar layout for social media elements using Flexbox.
- `.icons` class evenly spaces icons within a row, with margins above and below for visual separation.

### .buttons
- Applies top margin styling to button components for consistent vertical spacing.

# Usage Examples

To provide you with clear examples of how to use the aforementioned CSS classes, link to usage examples can be found here: [CSS Usage Examples](#).

- When designing a page, you can refer to the `.page` class to set up the structural grid.
- Titles and headers can be styled using the `.title` class for uniformity across your pages.
- Utilize the `.button-showcase` to group buttons and forms effectively with `.name-input`.
- For social media icon arrangements, use `.social-showcase` along with the `.icons` class for a clean layout.

Remember, when using these styles, the goal is coherence and visual balance. These styles should be mixed and matched to suit the specific needs of your content and overall page structure. Adjustments may be necessary for unique circumstances or responsive design considerations.

For further understanding and examples of CSS grid and flexbox, you can refer to the official documentation:
- [CSS Grid Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)
- [CSS Flexible Box Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout)