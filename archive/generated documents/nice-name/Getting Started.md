---
title: Getting Started
description: Guide for installing, setting up, and using your new Starlight documentation site.
---

# Installation and Setup

This guide will walk you through the process of getting your Starlight documentation site up and running.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Node.js:** Download and install the latest LTS version from https://nodejs.org/
*   **npm or yarn:** These package managers come bundled with Node.js. Verify installation by running `npm -v` or `yarn -v` in your terminal.

## Creating a New Project

1.  **Open your terminal** and navigate to the desired directory for your project.
2.  **Run the following command:**

```bash
npm create astro@latest -- --template starlight
```

    This will create a new Astro project using the Starlight documentation template.

3.  **Follow the prompts** to provide your project name and choose any additional features.
4.  **Navigate to your project directory:**

```bash
cd your-project-name
```

5.  **Install dependencies:**

```bash
npm install # or yarn install
```

## Running the Development Server

1.  **Start the development server:**

```bash
npm run dev # or yarn dev
```

    This command will start a local development server and open your documentation site in your default web browser. The site will typically be available at `http://localhost:3000`.

2.  **Edit your content:** Starlight looks for Markdown or MDX files in the `src/content/docs/` directory. You can edit existing files or add new ones to create and modify your documentation pages.

## Building for Production

1.  **Build your site:**

```bash
npm run build # or yarn build
```

    This command will generate a production-ready version of your site in the `dist/` directory.

2.  **Preview the build:**

```bash
npm run preview # or yarn preview
```

    This allows you to locally preview the generated site before deploying it.

## Deployment

Starlight documentation sites can be deployed to various hosting platforms. Refer to the specific platform's documentation for detailed instructions. Here are some popular options:

*   **Netlify:** https://www.netlify.com/
*   **Vercel:** https://vercel.com/
*   **GitHub Pages:** https://pages.github.com/
*   **AWS S3:** https://aws.amazon.com/s3/

# Basic Usage

## Content Structure

*   **`src/content/docs/`:** This directory holds your documentation content in Markdown or MDX format. Each file represents a page on your site.
*   **`src/assets/`:** Store images and other assets here, referenced within your Markdown files.
*   **`public/`:** Place static assets like favicons in this directory.

## Configuration

*   **`astro.config.mjs`:** Customize your site's title, social links, sidebar, and other configurations in this file.

## Writing Content

*   Use Markdown syntax for basic formatting.
*   Leverage MDX for advanced features like importing components or using JSX within your Markdown.
*   Reference images and assets using relative paths.

# Next Steps

*   Explore the Starlight documentation for more advanced features and customization options: https://starlight.astro.build/
*   Join the Astro Discord server for community support and discussions: https://astro.build/chat

