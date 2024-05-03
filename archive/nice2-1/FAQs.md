---
title: Frequently Asked Questions (FAQs)
description: Addressing common inquiries and providing helpful information related to the Starlight documentation site project. 
---

# Frequently Asked Questions (FAQs)

## General

*   **What is Astro?**

    Astro is a modern static site generator that enables developers to build fast, content-focused websites using UI components from various JavaScript frameworks or Astro's own templating language. 

*   **What is Starlight?**

    Starlight is an Astro integration designed specifically for building documentation websites. It provides features like content collections, automatic navigation, search, and theming. 

*   **What are the benefits of using a static site generator for documentation?**

    Static site generators offer advantages such as fast loading times, reduced server load, scalability, and improved security compared to dynamic websites. 

*   **Can I use my own CSS framework with Starlight?**

    Yes, you can use your preferred CSS framework or custom styles alongside Tailwind CSS, which is included by default in the Starlight documentation site project.

## Content and Navigation

*   **How do I add a new documentation page?**

    Create a new Markdown (`.md`) or MDX (`.mdx`) file within the `src/content/docs/` directory and include the necessary frontmatter to define the page's metadata. You may also need to update the sidebar configuration in `astro.config.mjs` to include the new page in the navigation. 

*   **How do I customize the sidebar navigation?**

    Modify the `sidebar` configuration object within the Starlight integration settings in the `astro.config.mjs` file. You can add, remove, or reorder sections and pages as needed. 

*   **How do I create links between pages?**

    Use Markdown link syntax (`[Link Text](link-url)`) to create links to other pages within your documentation site. Ensure that the link URLs are relative to the current page.

## Development and Deployment

*   **How do I start the development server?**

    Run `npm run dev` in your terminal to start the Astro development server. The documentation site will be available at `http://localhost:3000/`.

*   **How do I build the site for production?**

    Execute `npm run build` to generate the optimized static files in the `dist/` directory, ready for deployment.

*   **Where can I deploy my documentation site?**

    You can deploy your Starlight documentation site to various hosting platforms such as Netlify, Vercel, GitHub Pages, or any other static file hosting service.

## Troubleshooting

*   **I'm encountering errors during development or build. What should I do?**

    Refer to the "Troubleshooting Guide" section in the documentation for solutions to common issues. 

## Conclusion

This FAQ addresses frequently asked questions related to the Starlight documentation site project. If you have further inquiries, feel free to consult the Astro and Starlight documentation or seek assistance from the respective communities. 
