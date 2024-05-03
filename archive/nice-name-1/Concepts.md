---
title: Starlight Documentation Site Concepts
description: An exploration of the key concepts and principles behind Starlight documentation sites and their role in facilitating effective documentation creation.
---

# Key Concepts

## Static Site Generation

Starlight documentation sites leverage the power of static site generation (SSG) to transform plain text files (Markdown or MDX) into static HTML pages. This approach offers several advantages: 

* **Performance**: Static sites are inherently fast and efficient since the content is pre-rendered during the build process, eliminating the need for server-side processing or database queries on each request. 
* **Scalability**: Static sites can easily scale to handle large volumes of traffic due to their lightweight nature and ability to be served from content delivery networks (CDNs).
* **Security**:  With no dynamic server-side components or databases, static sites have a smaller attack surface, reducing the risk of security vulnerabilities.
* **Version Control**: Managing documentation content in plain text files simplifies version control and collaboration, enabling efficient tracking of changes and rollbacks when necessary. 

## Astro Framework

Starlight documentation sites are built upon the Astro framework (https://astro.build/), a modern static site generator known for its flexibility and performance. Astro enables you to:

* **Use your preferred UI framework**:  Incorporate UI components from popular frameworks like React, Vue, Svelte, or SolidJS within your documentation pages to create interactive and engaging experiences.
* **Leverage Markdown and MDX**: Write your documentation content in Markdown or MDX, combining the simplicity of Markdown with the ability to embed JSX components for dynamic elements.
* **Extend with Integrations**:  Extend the functionality of your documentation site using a wide range of Astro integrations for features such as search, analytics, and more. 

## Starlight Integration 

Starlight (https://starlight.astro.build/) is an Astro integration that provides a dedicated theme and features specifically designed for creating documentation sites. Starlight offers:

* **Themeable Design System**: A customizable design system that allows you to tailor the appearance and styling of your documentation site to match your brand or preferences.
* **Built-in Components**: A collection of pre-built components for common documentation elements such as navigation bars, sidebars, tables of contents, and code blocks, simplifying the development process.
* **Search Functionality**: Integrated search capabilities to help users quickly find relevant information within your documentation.
* **Versioning Support**: Features to facilitate versioning of your documentation content, enabling users to access documentation specific to different project versions.

## Design Principles

Starlight documentation sites are guided by several key design principles:

* **Simplicity**:  Starlight prioritizes a clean and uncluttered design, making it easy for users to focus on the documentation content without distractions.
* **Clarity**:  The documentation structure, layout, and writing style aim for clarity and conciseness, ensuring users can easily understand and follow the information presented.
* **Accessibility**: Starlight promotes accessibility by adhering to web standards and best practices, making the documentation usable by individuals with disabilities.
* **Customization**:  The themeable design system and configurable options empower you to tailor the documentation site to your specific requirements and preferences. 



