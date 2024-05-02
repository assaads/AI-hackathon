---
title: Starlight Documentation Site Configuration
description: An overview of key configuration options available in a Starlight documentation site project.
---

# Configuration

Starlight documentation sites offer several configuration options to customize the site's appearance, behavior, and features. These settings are primarily defined within the `astro.config.mjs` file located at the root of your project directory.

## Key Configuration Options

* **`site`**: Defines the base URL of your documentation site. This is essential for generating correct links and asset paths, especially when deploying to different environments or subdirectories.
* **`title`**: Sets the title of your documentation site, displayed in the browser tab and potentially within the site's header or navigation elements. 
* **`description`**: Provides a brief description of your documentation site, often used for SEO purposes and displayed in search engine results.
* **`lang`**: Specifies the primary language of your documentation content, which can be helpful for accessibility and internationalization.
* **`favicon`**:  Sets the path to your favicon file, which is the small icon displayed in the browser tab and bookmarks.
* **`theme`**:  (Optional) Allows you to customize the appearance and styling of your documentation site by overriding default theme variables or creating a custom theme. 
* **`markdown`**:  Provides options for configuring the Markdown rendering behavior, such as enabling specific extensions or customizing the syntax highlighting theme. 
* **`integrations`**:  Allows you to include and configure various Astro integrations to extend the functionality of your documentation site.  

## Starlight-Specific Options

Starlight introduces additional configuration options to tailor the documentation experience:

* **`sidebar`**: Defines the structure and content of the sidebar navigation. You can specify the hierarchy of sections, pages, and links to external resources.
* **`toc`**: Controls the behavior of the table of contents displayed on documentation pages. 
* **`previousNextLinks`**: Enables or disables the previous and next page links at the bottom of documentation pages.
* **`search`**:  Configures the built-in search functionality or integrates with a third-party search provider. 

## Example Configuration

```javascript
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  // Site-wide settings
  site: 'https://my-docs-site.com',
  title: 'My Awesome Docs',
  description: 'Documentation for my amazing project',
  lang: 'en',
  favicon: 'public/favicon.svg',

  // Starlight options
  integrations: [starlight({
    sidebar: {
      '/': [
        { text: 'Getting Started', link: 'getting-started' },
        { text: 'Guides', link: 'guides' },
        { text: 'Reference', link: 'reference' },
      ],
    },
  })],
});
```

## Additional Resources 

* **Starlight Documentation:** https://starlight.astro.build/
* **Astro Documentation:** https://docs.astro.build/


