---
title: Gemi-Doc Class and Module Documentation
description: Reference information for the classes and modules within the Gemi-Doc codebase, outlining their functionality and implementation details. 
---

# Class and Module Documentation

## Introduction

Gemi-Doc's codebase primarily consists of configuration files and Markdown/MDX content. The core functionality for building the documentation site is provided by the Astro framework and the Starlight integration. 

## Astro Framework

Astro is a static site generator that enables building fast, content-focused websites. It uses a component-based approach and supports various templating languages, including Markdown, MDX, and JSX.  

### Key Features

- **Component Islands:** Astro renders components on-demand, minimizing JavaScript usage and improving performance. 
- **Content Collections:** Astro allows organizing content into collections for easy management and retrieval. 
- **File-Based Routing:** Astro uses file names and directory structure to determine website routes, simplifying navigation and content organization. 

## Starlight Integration

Starlight is an Astro integration designed specifically for building documentation sites. It extends Astro's capabilities with features tailored for documentation, such as:

- **Sidebar Navigation:** Starlight provides a customizable sidebar for easy navigation through your documentation pages. 
- **Search Functionality:** Starlight enables adding a search bar to your site, allowing users to quickly find relevant information. 
- **Documentation-Specific Components:** Starlight includes components like `Card` and `CardGrid` that are useful for presenting documentation content.

## Tailwind CSS

Tailwind CSS is a utility-first CSS framework that provides a wide range of low-level CSS classes. This allows developers to build custom designs directly in their HTML without writing custom CSS. 

### Key Features 

- **Utility Classes:** Tailwind offers a comprehensive set of utility classes for styling typography, layout, spacing, color, and more. 
- **Responsiveness:** Tailwind's utility classes are designed to be responsive, making it easy to create websites that adapt to different screen sizes. 
- **Customization:** Tailwind's configuration file allows for extensive customization of the default theme and styles. 
