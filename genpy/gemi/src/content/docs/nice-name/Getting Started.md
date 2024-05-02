---
title: Getting Started with Starlight Documentation Site
description: A guide for installing, setting up, and initiating a new Starlight documentation site project.
---

# Getting Started

This guide provides instructions on how to set up and begin using a Starlight documentation site for your project.

## Prerequisites

Before starting, ensure you have the following installed:

* **Node.js:** Download and install the latest version of Node.js from https://nodejs.org/.
* **npm:** This comes bundled with Node.js. Verify the installation by running `npm -v` in your terminal. 

## Creating a New Project

1. **Open your terminal** and navigate to the desired directory for your project.
2. **Run the following command:**

```bash
npm create astro@latest -- --template starlight
```

3. **Follow the prompts** to name your project and select any optional features.

## Installation

1. Navigate to your project's root directory in the terminal. 
2. Run the following command to install the required dependencies:

```bash
npm install 
```

## Development Server

1. Start the development server using:

```bash
npm run dev
```

2. Access your documentation site at http://localhost:3000 in your web browser. 

## Building for Production

To create an optimized production build of your site:

```bash
npm run build
```

This generates the final static files in the `dist/` directory, ready for deployment.

## Project Structure

* **public/**: Contains static assets like favicons.
* **src/**: Holds the source code of your documentation site. 
    * **assets/**: Stores images and other assets used in your documentation.
    * **content/**: Houses the Markdown or MDX files that make up your documentation pages. 
        * **docs/**: The default location for your documentation content. 
    * **components/**:  (Optional) Can be used to store any reusable components for your documentation site.
* **astro.config.mjs**: Configuration file for Astro, including Starlight integration and optional features.
* **package.json**: Lists project dependencies and scripts.
* **tsconfig.json**: Configuration file for TypeScript (if used in your project). 

## Adding Content

* Create new Markdown (`.md`) or MDX (`.mdx`) files within the `src/content/docs/` directory. 
* Each file represents a documentation page, and its filename determines the route. 
* You can organize your content into subfolders within the `docs/` directory to create nested navigation structures.

## Customization

* Modify the `astro.config.mjs` file to configure your site's title, sidebar navigation, and other options. 
* Refer to the Starlight documentation (https://starlight.astro.build/) for detailed configuration options and features. 

## Next Steps

* Explore the example guide and reference pages provided in the `src/content/docs/` directory. 
* Start adding your own documentation content, tailoring it to your project's specific needs. 
* Customize the site's appearance and behavior through the configuration options available in Starlight. 
