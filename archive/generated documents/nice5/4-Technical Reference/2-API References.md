---
title: Gemi-Doc API References 
description: Documentation for the APIs available within the Gemi-Doc codebase, including their usage, parameters, and examples.
---

# Gemi-Doc API Reference

## Introduction

Gemi-Doc, being a static site generator, does not expose any external APIs for direct interaction. The primary way to interact with Gemi-Doc is through its command-line interface (CLI) and by editing the content and configuration files.

## Command-Line Interface (CLI)

The Gemi-Doc CLI provides commands for development, building, and previewing your documentation site.

### Available Commands

| Command        | Description                                      |
| -------------- | ------------------------------------------------ |
| `npm run dev`  | Starts the development server.                   |
| `npm run build` | Builds the documentation site for production.     |
| `npm run preview` | Previews the production build locally.          |

### Usage Examples

```bash
# Start the development server
npm run dev

# Build the documentation site for production
npm run build

# Preview the production build locally
npm run preview
```

## Configuration Options

Gemi-Doc's behavior and appearance can be customized through various configuration options in the `astro.config.mjs` file.

### Starlight Configuration

The `starlight` integration within Astro provides options for:

- `title`: Sets the title of your documentation site.
- `description`: Provides a description for your site.
- `baseUrl`: Specifies the base URL for your site.
- `sidebar`: Defines the structure and content of the sidebar navigation.
- `social`: Allows you to add links to your social media profiles. 

### Tailwind CSS Configuration

The `tailwind.config.mjs` file allows you to customize the Tailwind CSS configuration. You can add your own design tokens, modify the theme, and include additional plugins. 
