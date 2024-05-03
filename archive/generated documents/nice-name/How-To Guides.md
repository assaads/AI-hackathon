---
title: Customizing the Sidebar
description: Instructions for modifying the sidebar navigation in your Starlight documentation site. 
---

# Customizing the Sidebar

The sidebar is a crucial element of your Starlight documentation site, providing navigation and structure for your content. This guide explains how to customize the sidebar to match your project's organization and needs.

## Understanding the Sidebar Configuration

Starlight uses a `sidebar` option in the `astro.config.mjs` file to define the sidebar structure. The `sidebar` option is an array of objects, where each object represents a section in the sidebar.

Here's an example of a basic sidebar configuration:

```javascript
// astro.config.mjs
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  integrations: [starlight({
    // ... other configuration options
    sidebar: [
      {
        title: 'Getting Started',
        items: [
          { text: 'Introduction', link: '/' },
          { text: 'Installation', link: '/installation' },
        ],
      },
      {
        title: 'Guides',
        items: [
          { text: 'Guide 1', link: '/guide-1' },
          { text: 'Guide 2', link: '/guide-2' },
        ],
      },
    ],
  })],
});
```

## Adding and Editing Sidebar Sections

1. **Open the `astro.config.mjs` file** in your code editor.
2. **Locate the `sidebar` option** within the Starlight configuration. 
3. **To add a new section**, add a new object to the `sidebar` array. Each section object should have a `title` and an `items` array. The `items` array contains objects with `text` and `link` properties for each item within the section.
4. **To edit a section**, modify the existing section object's title or items. You can change the text, link, or order of items within a section.
5. **Save the `astro.config.mjs` file**. The changes to the sidebar will be reflected on your documentation site upon refresh.

## Example: Adding a "Reference" Section

To add a new section titled "Reference" with links to reference pages, you would modify the `sidebar` configuration as follows:

```javascript
sidebar: [
  // ... other sections
  {
    title: 'Reference',
    items: [
      { text: 'API Reference', link: '/api' },
      { text: 'Glossary', link: '/glossary' },
    ],
  },
],
```

## Advanced Sidebar Customization

*   **Nested sections:** You can create nested sections by adding an `items` array to an item within a section. This allows for hierarchical organization of your sidebar content.
*   **Collapsible sections:** To make sections collapsible, add a `collapsible` property set to `true` to the section object. 
*   **Custom icons:** You can add icons to sidebar items by specifying an `icon` property with the name of a Font Awesome icon.

## Additional Notes

*   The order of sections in the `sidebar` array determines their order in the sidebar navigation.
*   The links in the `items` array should correspond to the routes of your documentation pages.
*   Refer to the Starlight documentation for more information on sidebar customization options and examples.

