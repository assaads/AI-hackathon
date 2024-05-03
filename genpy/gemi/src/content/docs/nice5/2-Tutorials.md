---
title: Gemi-Doc Tutorials
description: Step-by-step guides to help you effectively utilize the features of Gemi-Doc for creating your documentation site.
---

## Creating and Editing Documentation Pages

### Adding New Pages

1. **Create a Markdown or MDX File:**
Within the `src/content/docs` directory, create a new file with the `.md` or `.mdx` extension. The file name will determine the URL path for the page. For example, `src/content/docs/getting-started.md` will be accessible at `/getting-started`.

2. **Add Frontmatter:**
At the beginning of your Markdown or MDX file, include frontmatter to specify page metadata. Here's an example: 

```
---
title: Getting Started
description: Learn how to set up and use Gemi-Doc.
---
```

3. **Write Content:** 
Use Markdown syntax to write your documentation content. You can include headings, paragraphs, code blocks, images, and links. 

### Editing Existing Pages

To edit an existing page, simply open the corresponding Markdown or MDX file in the `src/content/docs` directory and make the necessary changes. Save the file, and the updates will be reflected on your development site. 

## Organizing Content with the Sidebar

Gemi-Doc uses a sidebar for navigation. You can customize the sidebar structure and content in the `astro.config.mjs` file.  

### Modifying Sidebar Structure

The `sidebar` option in the Starlight configuration allows you to define the hierarchical structure of your documentation. 

```javascript
// astro.config.mjs
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  integrations: [starlight({
    // ... other options
    sidebar: {
      '/': [
        'index', 
        {
          text: 'Guides',
          children: [
            '/guides/install',
            '/guides/usage', 
          ], 
        },
      ], 
    },
  })],
});
```

In this example, the sidebar will have two top-level items: "index" (referring to `src/content/docs/index.mdx`) and "Guides," which is a section containing two child pages. 


