---
title: Gemi-Doc Function and Method Documentation 
description: Detailed information on the functions and methods within the Gemi-Doc codebase, including their purpose, parameters, return values, and potential exceptions. 
---

# Function and Method Documentation

## Introduction

Gemi-Doc primarily utilizes the functionalities provided by the Astro framework and the Starlight integration. As a static site generator, the codebase itself does not contain extensive custom functions or methods. The main logic resides in the configuration files and the Markdown/MDX content processing. 

## Astro Framework Functions and Methods

The Astro framework provides various functions and methods for building static websites. Some of the commonly used ones include:

- **`defineConfig`:** This function is used to define the Astro configuration, including integrations, build options, and adapter settings. 

```javascript
// astro.config.mjs
import { defineConfig } from 'astro/config'; 
// ... other imports 

export default defineConfig({
  // ... configuration options
});
```

- **`defineCollection`:** This function defines a content collection within Astro, specifying the schema and other options for managing content.

```javascript 
// src/content/config.ts
import { defineCollection } from 'astro:content';
// ... other imports 

export const collections = {
  docs: defineCollection({
    // ... collection options
  }),
};
```

## Starlight Integration Functions and Methods

The Starlight integration extends Astro with documentation-specific functionalities. Key functions and methods include:

- **`starlight()`:** This function initializes the Starlight integration within the Astro configuration, allowing you to set options like `title`, `sidebar`, and `social` links. 

```javascript
// astro.config.mjs
import starlight from '@astrojs/starlight'; 
// ... other imports

export default defineConfig({
  integrations: [starlight({
    // ... Starlight configuration options
  })], 
});
```

## Content Processing Functions

- **`remark` and `rehype` Plugins:** These libraries provide various plugins for processing Markdown and HTML content. For example, `remark-gfm` enables support for GitHub Flavored Markdown, and `rehype-raw` allows including raw HTML within Markdown. 

## Additional Notes

- The specific functions and methods used in a Gemi-Doc project may vary depending on the chosen integrations and customizations.
- Refer to the official documentation for Astro, Starlight, and other relevant libraries for more detailed information on their APIs and usage. 
