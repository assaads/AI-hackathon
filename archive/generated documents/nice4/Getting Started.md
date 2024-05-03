---
title: Getting Started with Starlight Docs
description: A guide to install, set up, and begin using Starlight for your documentation site.
---

# Getting Started with Starlight Docs

This guide will walk you through the process of installing, setting up, and getting started with Starlight to build your documentation site. 

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Node.js:** Download and install the latest LTS version of Node.js from https://nodejs.org/.

## Installation

1. **Create a new project:** Open your terminal and run the following command:

```bash
npm create astro@latest -- --template starlight
```
This command utilizes `npm` (Node Package Manager) to create a new Astro project using the Starlight template. 

2. **Install dependencies:** Navigate to your project directory and install the required dependencies: 

```bash
npm install 
``` 

## Project Structure

After installation, your project will have the following structure:

```
.
├── public/ 
├── src/
│   ├── assets/
│   ├── content/
│   │   └── docs/
│   └── env.d.ts
├── astro.config.mjs
├── package.json
└── tsconfig.json

```

- **public/**: This folder contains static assets such as favicons. 
- **src/assets/**: Store images and other assets used in your documentation within this folder. 
- **src/content/**: This folder holds your Markdown (`.md`) or MDX (`.mdx`) files, which define the content of your documentation site. Starlight specifically looks for files within the `src/content/docs/` directory. 
- **astro.config.mjs**: This file allows you to configure various aspects of your Starlight project, including the sidebar, navigation, and site title.
- **package.json**: This file manages your project's dependencies and scripts. 
- **tsconfig.json**: This file configures the TypeScript compiler for your project. 

## Running the Development Server 

1. **Start the development server:** In your terminal, run the following command:

```bash
npm run dev 
```

2. **Access your site:** Open your web browser and navigate to http://localhost:3000/ to view your Starlight documentation site. 

## Building for Production

1. **Build your site:** When you are ready to deploy your documentation site, run the following command to generate the production-ready files:

```bash
npm run build
```

2. **Preview your site:** Before deploying, you can preview the production build locally using this command: 

```bash
npm run preview 
```

## Next Steps

- **Customize your content:** Edit or add Markdown/MDX files in the `src/content/docs/` directory to create and modify your documentation pages. 
- **Configure your site:** Explore the `astro.config.mjs` file to personalize your site's title, sidebar, navigation, and other settings. 
- **Learn more:** Refer to the official Starlight documentation at https://starlight.astro.build/ for in-depth information and advanced features. 



