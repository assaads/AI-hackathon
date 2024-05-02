---
title: Starlight Documentation Site Component Architecture
description: A high-level overview of the main components within a Starlight documentation site project.
---

# Component Architecture 

## Overview

A Starlight documentation site consists of several key components that work together to create and serve the documentation content:

* **Astro**: The underlying static site generator that renders the documentation pages. 
* **Starlight**: An Astro integration that provides the documentation theme, layout, and features.
* **Content**: Markdown (`.md`) or MDX (`.mdx`) files containing the actual documentation content.
* **Assets**: Images, videos, or other media files used within the documentation.
* **Configuration**: The `astro.config.mjs` file where you define site settings and customizations. 

## ASCII Diagram

```
+-----------------+    +-----------------+    +--------------+
|     Astro       |    |   Starlight    |    |   Content   |
|                 |    |                 |    | (Markdown/  |
| (Static Site    |    | (Theme, Layout,|    |   MDX)      |
|  Generator)     |    |   Features)     |    |--------------+
+-----------------+    +-----------------+    +--------------+
       ^                  ^                  ^
       |                  |                  |
+-----------------+    +--------------+    +--------------+
|   Configuration  |    |   Assets    |    |    User     |
|  (astro.config.mjs)|    | (Images,    |    | (Browser)   |
|                 |    |  Videos, etc)|    |--------------+
+-----------------+    +--------------+ 
```

## Component Interactions

1. **Content Processing:** Astro processes the Markdown/MDX content files.
2. **Page Generation:** Astro utilizes Starlight to generate static HTML pages for each documentation page.
3. **Asset Integration:** Starlight incorporates assets into the generated pages as needed. 
4. **Configuration Application:** Astro applies the settings and customizations defined in the `astro.config.mjs` file.
5. **Serving Content:** The generated static HTML pages and assets are served to users' web browsers.

## Additional Components

* **Third-Party Integrations:** Starlight supports various third-party integrations for search, analytics, and other functionalities. 
* **Custom Components:** Developers can create and integrate custom components to extend the functionality or appearance of the documentation site. 


