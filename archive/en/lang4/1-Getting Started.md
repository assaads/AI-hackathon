---
title: Getting Started with Starlight Documentation Project
description: A comprehensive guide to install, set up, and begin using Starlight for your documentation needs.
---

## Prerequisites

Before diving into the setup process, ensure you have the following prerequisites installed on your system:

*   **Node.js**: Download and install the latest LTS version of Node.js from the official website (https://nodejs.org/).

## Installation

1.  **Create a new project**: Open your terminal and execute the following command:

```bash
npm create astro@latest my-docs-project -- --template starlight
```

This command utilizes the Astro CLI to create a new project directory named `my-docs-project` and initializes it with the Starlight template.

2.  **Navigate to the project directory**:

```bash
cd my-docs-project
```

3.  **Install dependencies**:

```bash
npm install
```

This command installs all the necessary dependencies required for the Starlight project to function correctly.

## Project Structure

Once the installation is complete, familiarize yourself with the project structure:

```
my-docs-project/
├── public/
│   └── favicon.svg
├── src/
│   ├── assets/
│   │   └── houston.webp
│   ├── content/
│   │   └── docs/
│   │       ├── guides/
│   │       │   └── example.md
│   │       ├── index.mdx
│   │       └── reference/
│   │           └── example.md
│   └── env.d.ts
├── astro.config.mjs
├── package-lock.json
├── package.json
├── README.md
├── tailwind.config.mjs
└── tsconfig.json

```

*   **`public/`**: Stores static assets such as favicon.
*   **`src/assets/`**: Contains images and other assets used in your documentation.
*   **`src/content/`**: Houses your Markdown or MDX files that make up the documentation content. 
*   **`src/content/docs/`**: The default location where Starlight looks for Markdown or MDX files.
*   **`astro.config.mjs`**:  Configures site-wide settings and integrations for Starlight.
*   **`package.json`**: Defines project metadata and dependencies.
*   **`tsconfig.json`**: Configuration for TypeScript (if used). 

## Running the Development Server

1.  **Start the development server**:

```bash
npm run dev
```

This command launches the development server, typically at `http://localhost:4321/`. Open your web browser and navigate to this address to view your Starlight documentation site.

2.  **Edit content**: As you make changes to your Markdown or MDX files within the `src/content/docs/` directory, the development server will automatically rebuild and update the site in your browser, allowing you to see the changes in real-time. 

## Building for Production

1.  **Build the site**: When you're ready to deploy your documentation site, run the following command:

```bash
npm run build
```

This command generates a production-ready version of your site within the `dist/` directory. 
