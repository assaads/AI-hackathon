---
title: Troubleshooting Guide - Starlight Documentation Site
description: Addressing common issues that may arise during the development or usage of your Starlight documentation site.
---

# Troubleshooting Guide 

This guide provides solutions to common problems you might encounter while working with the Starlight documentation site project.

## Development and Build Issues

*   **`npm install` errors:**
    *   **Network connectivity:** Ensure you have a stable internet connection.
    *   **Permissions:** Verify that you have the necessary permissions to install packages in the project directory. 
    *   **Package versions:** Check for compatibility issues between package versions in your `package.json` file. 
*   **`npm run dev` or `npm run build` errors:**
    *   **Code syntax:**  Carefully review your Markdown, MDX, and JavaScript code for any syntax errors.
    *   **Configuration:** Double-check your configuration files (`astro.config.mjs`, `tailwind.config.js`) for typos or incorrect settings.
    *   **Dependencies:** Ensure all dependencies are installed correctly and are compatible with your project.
*   **Tailwind CSS styling issues:**
    *   **Class names:** Verify that you are using the correct Tailwind CSS class names. Refer to the Tailwind documentation for reference.
    *   **Configuration:** Check your `tailwind.config.js` file to ensure that the necessary files are included in the `content` array for Tailwind to scan.
    *   **Build process:** Make sure you are running `npm run dev` or `npm run build` to generate the Tailwind CSS styles.

## Content and Navigation Issues

*   **New pages not appearing in navigation:**
    *   **Sidebar configuration:** Ensure that you have added the new page to the `sidebar` configuration in your `astro.config.mjs` file.
*   **Broken links:**
    *   **File paths:** Verify that the file paths in your links are correct and relative to the current page. 

## Deployment Issues

*   **404 errors after deployment:**
    *   **Base URL:** If your site is deployed to a subdirectory, ensure that you have set the correct base URL in your Astro configuration or hosting provider settings.
*   **Missing assets:**
    *   **Asset paths:**  Double-check that the paths to your assets (images, fonts) are correct and accessible from the deployed location.

## General Troubleshooting Tips

*   **Clear cache:** Clear your browser cache and any build caches (e.g., Astro's `.astro` cache directory) to ensure you are viewing the latest changes.
*   **Restart server:** Restart the development server to resolve any temporary issues. 
*   **Check logs:** Review the console output or server logs for more detailed error messages or clues about the problem.
*   **Search online resources:** Look for solutions or similar issues reported in online forums, communities, or the Astro and Starlight documentation.

## Conclusion 

By following this troubleshooting guide and referring to the available resources, you should be able to effectively address common problems encountered while using the Starlight documentation site project. 
