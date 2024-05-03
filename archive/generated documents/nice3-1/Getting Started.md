---
title: Getting Started with Starlight Documentation Project
description: A comprehensive guide to install, set up, and begin using the Starlight documentation project.
---

# Prerequisites
Before diving in, ensure you have the following tools installed on your system:

- **Node.js**: Download and install the latest LTS version of Node.js from https://nodejs.org/.
- **npm**: Node Package Manager comes bundled with Node.js and is used for managing project dependencies.

# Installation
1. **Create a new project**: Use the Astro CLI to create a new project with the Starlight template. Open your terminal and run the following command:

```bash
npm create astro@latest -- --template starlight
```

2. **Navigate to the project directory**:

```bash
cd your-project-name 
```

3. **Install dependencies**: Install the required project dependencies using npm:

```bash
npm install
```

# Project Structure
Familiarize yourself with the project's file and folder structure:

```
.
├── public/      # Static assets like favicons
├── src/
│   ├── assets/  # Images and other assets used in your documentation
│   └── content/
│       └── docs/ # Markdown or MDX files for documentation pages
├── astro.config.mjs   # Astro configuration file
├── package.json        # Project dependencies and scripts
└── tsconfig.json       # TypeScript configuration
```

# Running the Development Server 
Start the local development server to view and interact with your documentation site:

```bash
npm run dev
```

This command launches a development server typically at `http://localhost:4321/`. Open this URL in your web browser to see your documentation site. As you make changes to your content or code, the site automatically updates in the browser.

# Building for Production 
When you are ready to deploy your documentation site, build the production-ready static files:

```bash
npm run build
```

This command generates optimized static files in the `dist/` directory, which you can then deploy to any static web hosting service. 

# Next Steps
- **Customize Content**: Edit the existing Markdown or MDX files in the `src/content/docs/` directory to add your own documentation content.
- **Configure Navigation**: Modify the `astro.config.mjs` file to customize the navigation sidebar and other site settings.
- **Explore Starlight**: Refer to the Starlight documentation (https://starlight.astro.build/) for more advanced features and customization options. 

# Additional Resources
- **Astro Documentation**: https://docs.astro.build/
- **Tailwind CSS Documentation**: https://tailwindcss.com/docs/ 
