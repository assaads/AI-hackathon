---
title: How-To Guides for the Starlight Documentation Site
description: This section will provide instructions for common tasks related to building and customizing your documentation site with Starlight.
---

# How-To Guides

These guides offer step-by-step instructions for accomplishing specific tasks related to building and managing your Starlight documentation site.

## Adding a New Documentation Page

1.  **Create a new file:** Inside the `src/content/docs/` directory, create a new file with a descriptive name using either the `.md` (Markdown) or `.mdx` (MDX) extension. For example, `new-feature.md`. 

2.  **Add frontmatter:** At the beginning of the file, include frontmatter to define the page's metadata. The following frontmatter properties are essential:

*   `title`: The title of the page as it will appear in the navigation and page header.
*   `description`: A brief description of the page's content. 

```markdown
---
title: New Feature Guide
description: Learn how to use the exciting new feature.
---
```

3.  **Write your content:** Below the frontmatter, write the content of your documentation page using Markdown or MDX syntax. You can structure your content with headings, paragraphs, code blocks, images, and other elements as needed.

4.  **Include the page in the sidebar (optional):** To make the new page appear in the sidebar navigation, you need to add it to the `sidebar` configuration within the `astro.config.mjs` file. 

```javascript
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// ... other imports

export default defineConfig({
  integrations: [
    starlight({
      // ... other Starlight config
      sidebar: {
        '/': [
          { text: 'Getting Started', link: '/' },
          { text: 'Guides', link: '/guides/' },
          { text: 'New Feature Guide', link: '/guides/new-feature' }, // Add your new page
          // ... other sidebar items
        ],
      },
    }),
  ],
});
```

## Customizing the Sidebar Navigation

1.  **Open `astro.config.mjs`:** Locate the `sidebar` configuration object within the Starlight integration settings.

2.  **Modify the structure:** The `sidebar` object is typically an object where each key represents a section of the documentation, and the corresponding value is an array of objects describing the pages within that section. Each page object should have `text` (the displayed text) and `link` (the URL path) properties. 

```javascript
sidebar: {
  '/': [
    { text: 'Section 1', header: true }, // Optional header for a section
    { text: 'Page 1', link: '/page-1' },
    { text: 'Page 2', link: '/page-2' },
  ],
  '/guides/': [
    { text: 'Guide 1', link: '/guides/guide-1' },
    { text: 'Guide 2', link: '/guides/guide-2' }, 
  ], 
},
```

3.  **Add or remove sections and pages:** You can add new sections by creating new keys in the `sidebar` object and populating them with page objects. Similarly, remove sections or pages by deleting the corresponding keys or page objects.

4.  **Reorder pages:** Change the order of pages within a section by rearranging the page objects within the array. 

5.  **Save and refresh:** Save the changes to `astro.config.mjs` and refresh the documentation site in your browser to see the updated sidebar navigation.

## Styling with Tailwind CSS 

1.  **Identify elements to style:** Determine the specific elements you want to style using Tailwind CSS. This could include headings, paragraphs, buttons, code blocks, or any other HTML element on your page. 

2.  **Apply Tailwind classes:** Refer to the Tailwind CSS documentation (https://tailwindcss.com/docs) to find the appropriate utility classes for your desired styles. Add these classes directly to the HTML elements in your Markdown or MDX files. For example:

```markdown
<h1 class="text-3xl font-bold mb-4">This is a styled heading</h1>
<p class="text-lg text-gray-700">This is a styled paragraph.</p>
```

3.  **Customize the theme (optional):**  If you need more control over the styling, you can customize the Tailwind theme by editing the `tailwind.config.mjs` file. This allows you to define your own color palettes, font sizes, spacing scales, and more.

## Conclusion

These how-to guides provide a starting point for building and customizing your Starlight documentation site. As you become more familiar with the project and its capabilities, you can explore additional customization options and features to create a comprehensive and user-friendly documentation experience. 
