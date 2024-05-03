---
title: Configuration Files Overview
description: Explanation of configuration files within the Starlight documentation project. 
---

# Astro Configuration File (`astro.config.mjs`)

This file is central to setting up and customizing your Astro project.  Key sections include:

## `import` Statements

* Import necessary functions and integrations from Astro and other packages. Example:

```javascript
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import tailwind from "@astrojs/tailwind";
```

## `defineConfig` Function

* Defines and exports the project configuration object. 

## `integrations` Array

* Specifies the Astro integrations used in the project. Example:

```javascript
integrations: [
    starlight({ ... }),
    tailwind({ ... })
]
```

### Starlight Integration Options

* **`title`** (string): Sets the title of your documentation site.
* **`social`** (object): Contains social media links. 
    * **`github`** (string): URL of your project's GitHub repository.

### Tailwind CSS Integration Options

* **`config`** (string): Path to your Tailwind config file (optional).
* **`applyBaseStyles`** (boolean): Whether to apply Tailwind's base styles (optional). 

# Tailwind Configuration File (`tailwind.config.js` or `tailwind.config.cjs`)

This file customizes Tailwind's default settings and behavior. Key sections:

## `content` Array

* Specifies the files Tailwind should scan for class names. Example:

```javascript
content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
```

## `theme` Object

* Customizes Tailwind's design system, including colors, fonts, spacing, etc.

## `plugins` Array

* Includes additional Tailwind plugins for extended functionality. 

# Content Collection Configuration (`src/content/config.ts`)

This file defines content collections using Astro's `defineCollection` function. Example:

```typescript
import { defineCollection } from 'astro:content'; 
import { docsSchema } from '@astrojs/starlight/schema'; 

export const collections = {
    docs: defineCollection({ schema: docsSchema() }),
};
```

* **`docs`**: A collection named "docs" using the schema provided by Starlight. You can define additional collections with custom schemas as needed. 

# TypeScript Configuration File (`tsconfig.json`)

This file configures the TypeScript compiler options for the project.  It typically extends Astro's recommended configuration for strict type checking. 
