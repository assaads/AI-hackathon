---
title: Getting Started with Gemi-Doc
description: A comprehensive guide to installing, setting up, and using Gemi-Doc for building your documentation site. 
---

# Introduction 

Welcome to Gemi-Doc, a documentation site generator powered by Astro and Starlight. This guide will walk you through the process of getting your Gemi-Doc project up and running quickly. 

## Prerequisites

Before you begin, ensure you have the following tools installed on your system:

- **Node.js:** Gemi-Doc requires Node.js version 18.17.1, 20.3.0, or later. Download and install the appropriate version from the official Node.js website: https://nodejs.org/
- **npm or yarn:** Gemi-Doc uses `npm` (Node Package Manager) or `yarn` for managing dependencies. These tools are typically included with your Node.js installation. 

## Installation

1. **Create a New Project:**
Open your terminal and run the following command to create a new Gemi-Doc project:

```bash
npm create astro@latest -- --template starlight
``` 

2. **Navigate to Project Directory:**
```bash
cd gemi-doc 
```

3. **Install Dependencies:**
Use either `npm` or `yarn` to install the required dependencies: 

```bash
npm install 
```

or 

```bash
yarn install 
```

## Running the Development Server

Start the development server to view your documentation site locally: 

```bash
npm run dev 
```

This command will launch a local server, typically at `http://localhost:4321/`. Open this URL in your web browser to see your Gemi-Doc site. 

## Building for Production 

When you're ready to deploy your documentation site, run the following command to create an optimized production build: 

```bash 
npm run build 
```

The generated static files will be located in the `dist/` directory, ready to be deployed to your preferred hosting platform. 
