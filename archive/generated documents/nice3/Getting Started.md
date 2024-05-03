"
---
title: Getting Started with Starlight Documentation Site
description: A comprehensive guide to installing, setting up, and initiating your Starlight documentation site project.
---

# Getting Started 

This guide will walk you through the process of setting up and using a new Starlight documentation site. 

## Prerequisites

Before you begin, ensure you have the following software installed on your system:

*   **Node.js**: Download and install the latest LTS version of Node.js from https://nodejs.org/. 
*   **npm**: This comes bundled with Node.js. Verify the installation by running `npm -v` in your terminal. 

## Creating a New Project

1.  **Open your terminal** and navigate to the directory where you want to create your project.
2.  **Run the following command** to create a new Astro project using the Starlight template:

```bash
npm create astro@latest -- --template starlight
```

3.  **Follow the prompts** to provide your project name and select desired options. 
4.  **Navigate to the project directory**:

```bash
cd your-project-name
```

5.  **Install dependencies**:

```bash
npm install
```

## Running the Development Server

1.  **Start the development server**:

```bash
npm run dev
```

2.  **Open your web browser** and visit `http://localhost:3000` to view your Starlight documentation site. 

## Project Structure

Here's a breakdown of the key folders and files in your project: 

*   **public/**: This folder contains static assets such as images, favicons, and robots.txt.
*   **src/**: The source code of your documentation site resides here. 
    *   **assets/**: Store images and other assets that you reference in your Markdown or MDX files.
    *   **components/**: You can create reusable components for your documentation site here.
    *   **content/**: This folder holds the Markdown or MDX files that will be converted into documentation pages. 
        *   **docs/**: Place your documentation files here. Each file represents a page on your site. 
    *   **layouts/**: Define layout templates for your documentation pages here. 
*   **astro.config.mjs**: Configure your site settings, including the site title, sidebar navigation, and social links. 
*   **package.json**: Lists the project dependencies and scripts. 
*   **tsconfig.json**: Configuration for TypeScript (if used in your project). 

## Adding Content 

1.  **Create new Markdown (`.md`) or MDX (`.mdx`) files** in the `src/content/docs/` directory. 
2.  **Write your documentation content** using Markdown syntax. 
3.  **Use frontmatter** at the beginning of each file to specify page metadata, such as the title and description.

```markdown
---
title: My First Page
description: This is an example documentation page.
---

# Welcome to my documentation!
```

## Building for Production

1.  **Run the build command**:

```bash
npm run build
```

2.  This will create a production-ready version of your site in the `dist/` directory. 

## Deployment 

Starlight documentation sites can be deployed to various static hosting platforms such as Netlify, Vercel, or GitHub Pages. Consult the documentation of your chosen platform for specific deployment instructions. 

## Additional Resources

*   [Starlight Documentation](https://starlight.astro.build/)
*   [Astro Documentation](https://docs.astro.build)
"
