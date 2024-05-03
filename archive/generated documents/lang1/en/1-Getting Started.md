---
title: Getting Started with Starlight
description: Learn how to install, set up, and start using Starlight to build your documentation site. 
---

## Setting Up Your Starlight Project

### Prerequisites

Before you begin, ensure you have the following tools installed:

* **Node.js:** Starlight is built on Node.js, so you'll need to have it installed on your system. Download and install the latest LTS version from the official Node.js website: https://nodejs.org/

### Installation

1. **Create a new project:** Open your terminal and run the following command to create a new Starlight project using the Astro CLI:

```bash
npm create astro@latest -- --template starlight
```

2. **Install dependencies:** Navigate to your newly created project directory and install the required dependencies:

```bash
npm install
``` 

## Starting the Development Server

1. **Run the development server:** Use the following command to start the local development server:

```bash
npm run dev
```

2. **Access your site:** Once the server is running, you can access your Starlight documentation site at `http://localhost:4321` in your web browser. 

## Building for Production

1. **Build your site:** When you're ready to deploy your documentation site, run the build command:

```bash
npm run build
```

2. **Production files:** This command will generate the production-ready files in the `dist/` directory within your project. You can then deploy this directory to a static hosting service. 
