---
title: Configuration Files: astro.config.mjs
description: A guide to configuring your Starlight project using the astro.config.mjs file.
---

## astro.config.mjs

The `astro.config.mjs` file serves as the central hub for configuring various aspects of your Starlight project. It allows you to define site metadata, integrate external tools, customize build settings, and more.

### Site Metadata

*   **site**: (string) Specifies the base URL of your website. This is essential for generating correct URLs for internal links and assets.

```javascript
export default defineConfig({
  // ... other configuration options
  site: 'https://example.com', // Replace with your domain
});
```

### Content Options

*   **markdown**: (object) Configures options related to Markdown processing. 
    *   **shikiConfig**: (object) Allows customization of code highlighting using the Shiki library. You can specify the desired theme and other options.

```javascript
export default defineConfig({
  // ... other configuration options
  markdown: {
    shikiConfig: {
      theme: 'dracula', // Set the code highlighting theme
    },
  },
});
```

### Starlight Options

*   **starlight()**:  A function that accepts an options object to configure Starlight-specific settings.
    *   **sidebar**: (array) Defines the structure and content of the sidebar navigation. Each element in the array represents a section or page, with properties like `title` and `link`. 

```javascript
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  // ... other configuration options
  integrations: [starlight({
    // ... other Starlight options
    sidebar: [
      {
        title: 'Section 1',
        items: [
          { title: 'Page 1', link: '/page-1' },
          { title: 'Page 2', link: '/page-2' },
        ],
      },
      // ... more sidebar sections
    ],
  })],
});
```

## Additional Configuration Options

The `astro.config.mjs` file offers numerous other configuration options to tailor your project to your specific needs. Refer to the official [Astro documentation](https://docs.astro.build/en/reference/configuration-reference/) for a comprehensive list and detailed explanations. 


