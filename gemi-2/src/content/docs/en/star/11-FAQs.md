---
title: Frequently Asked Questions (FAQs)
description: Answers to common inquiries about the Starlight project.
---

## General

*   **What is Starlight?**

    Starlight is a static site generator built on top of the Astro framework, specifically designed for creating documentation websites. It simplifies the process of building and maintaining documentation by providing a structured approach, pre-built components, and convenient features. 
*   **Why should I use Starlight?**

    Starlight offers several advantages for building documentation:

    *   **Simplicity:** Easy to set up and use, even for users with limited technical expertise.
    *   **Content-Focused:** Emphasizes a content-first approach, allowing you to focus on writing and managing your documentation.
    *   **Performance:** Generates static HTML files, resulting in fast loading times and excellent performance. 
    *   **Customization:** Provides various configuration options to tailor the appearance and functionality of your site.
    *   **Community and Support:** Backed by the active Astro community and comprehensive documentation.

*   **What are the prerequisites for using Starlight?**

    To use Starlight, you need to have Node.js (version 14 or later) and a package manager like npm or yarn installed on your system. 

## Content and Configuration

*   **How do I edit existing content?**

    Navigate to the `src/content/` directory and edit the Markdown or MDX files using your preferred text editor. Changes will be reflected automatically on the development site.
*   **How do I add new pages?**

    Create new Markdown or MDX files within the `src/content/` directory. Include frontmatter at the beginning of each file to specify attributes like title and description.
*   **How do I customize the site's metadata?**

    Edit the `site` property in the `astro.config.mjs` file to modify the title, description, and other metadata for your site.
*   **How do I add a sidebar?**

    Configure the `sidebar` option within the `starlight` property in the `astro.config.mjs` file. Define an array of objects representing sections and pages for your sidebar navigation.

## Development and Deployment

*   **How do I run the development server?**

    Use the command `npm run dev` or `yarn dev` to start the development server. Access your site at `http://localhost:3000`.
*   **How do I deploy my Starlight site?**

    Choose a hosting provider like Netlify, Vercel, or GitHub Pages. Configure the deployment settings, connect to your Git repository, and initiate the deployment process.

## Troubleshooting

*   **What should I do if the development server is not starting?**

    Check for port conflicts, ensure all dependencies are installed correctly, and review your `astro.config.mjs` file for any errors. 
*   **What should I do if content changes are not reflecting?**

    Clear your browser cache or restart the development server. Verify that you are editing the correct files and that the file paths in your configuration are accurate.
*   **What should I do if I encounter OpenAI API errors?**

    Refer to the dedicated section on "Error Codes and Messages" in the documentation for guidance on troubleshooting common OpenAI API errors. 


