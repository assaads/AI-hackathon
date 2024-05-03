---
title: Starlight Documentation Tutorials
description: Step-by-step guides to effectively utilize the features of Starlight for building your documentation site.
---

## Creating and Editing Documentation Pages

Starlight primarily uses Markdown (`.md`) or MDX (`.mdx`) files to create documentation pages. These files should be placed within the `src/content/docs/` directory. The file name determines the URL path for each page.

### Creating a New Page

1.  **Create a new file**: Within the `src/content/docs/` directory, create a new file with a descriptive name using either the `.md` or `.mdx` extension. For example, `new-feature.md`.
2.  **Add content**: Write your documentation content using Markdown syntax. You can include headings, paragraphs, code blocks, images, and other Markdown elements.

### Editing an Existing Page

1.  **Locate the file**: Find the Markdown or MDX file you want to edit within the `src/content/docs/` directory.
2.  **Make changes**: Open the file in a text editor and modify the content as needed. 

## Structuring Your Documentation

Starlight offers flexibility in organizing your documentation using folders within the `src/content/docs/` directory. This allows you to create a hierarchical structure for your content.

### Creating Sections

1.  **Create a folder**: Within the `src/content/docs/` directory, create a new folder for each section of your documentation. For example, `guides/` or `reference/`.
2.  **Add pages**: Inside each section folder, create Markdown or MDX files for the individual pages within that section. 

## Adding Images

Enhance your documentation with images by placing them in the `src/assets/` directory and referencing them within your Markdown content.

### Embedding an Image

```markdown
![Image description](../assets/image.png)
```

## Configuration Options

Explore the `astro.config.mjs` file to customize various aspects of your Starlight documentation site. Refer to the Starlight Project Configuration Guide for detailed information on available options. 
