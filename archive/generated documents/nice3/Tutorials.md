"
---
title: Starlight Tutorials: Mastering Documentation Creation 
description: A collection of step-by-step tutorials to guide you through the process of building and customizing your Starlight documentation site.
---

# Tutorials

This section provides hands-on tutorials to help you effectively use Starlight for creating and managing your documentation site.

## Tutorial 1: Creating Your First Documentation Page

1.  **Navigate to the `src/content/docs/` directory** in your Starlight project.
2.  **Create a new Markdown file** named `my-first-page.md`.
3.  **Add the following frontmatter** to the beginning of the file:

```markdown
---
title: My First Page
description: A beginner's guide to creating a documentation page in Starlight.
---
```

4.  **Write your documentation content** using Markdown syntax. For example: 

```markdown
# Welcome to My Documentation! 

This is my first documentation page built with Starlight. 
```

5.  **Save the file**. Your new documentation page will be accessible at `http://localhost:3000/my-first-page` when you run the development server.

## Tutorial 2: Structuring Your Documentation with Sections

1.  **Create a new folder** within the `src/content/docs/` directory to represent a section. For example, create a folder named `getting-started`.
2.  **Inside the new folder, create Markdown files** for each documentation page within that section. For example, create files named `installation.md` and `configuration.md`. 
3.  **Add frontmatter** to each file as shown in Tutorial 1. 
4.  **Organize your content** within each page using Markdown headings, lists, and code blocks. 

## Tutorial 3: Customizing the Sidebar Navigation

1.  **Open the `astro.config.mjs` file**.
2.  **Locate the `starlight` configuration object**.
3.  **Modify the `sidebar` property** to define the structure of your sidebar navigation. 
4.  **Use an array of objects** to represent sections and pages. Each object should have a `title` and a `link` property. For nested structures, use the `items` property to define sub-pages within a section. 

```javascript
// astro.config.mjs
import starlight from '@astrojs/starlight';

export default defineConfig({
  integrations: [starlight({
    // ... other configuration
    sidebar: [
      {
        title: 'Getting Started',
        link: '/getting-started/installation'
      },
      {
        title: 'Features',
        link: '/features/overview',
        items: [
          { title: 'Feature A', link: '/features/feature-a' },
          { title: 'Feature B', link: '/features/feature-b' },
        ]
      }
    ]
  })]
});
```

## Tutorial 4: Adding Images and Assets

1.  **Place your image files** in the `src/assets/` directory. 
2.  **In your Markdown files, use relative paths** to reference the images. 

```markdown
![Image of my project](../assets/my-image.png)
```

## Tutorial 5: Utilizing MDX for Advanced Content

1.  **Create MDX files (`.mdx`)** instead of Markdown files when you need to include interactive components or advanced formatting.
2.  **Import React components** from your project or from third-party libraries.
3.  **Use JSX syntax** to embed components within your MDX content.

## Conclusion

These tutorials provide a starting point for building and customizing your Starlight documentation site. As you explore the capabilities of Starlight and Astro, you can create comprehensive and engaging documentation for your projects.
"
