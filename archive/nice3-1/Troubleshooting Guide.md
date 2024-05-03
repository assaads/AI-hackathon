---
title: Troubleshooting Guide
description: Solutions to common issues encountered while using the Starlight documentation project.
---

## Build Process Issues

### `Error: Cannot find module '...'`

* **Cause**: A required dependency is missing.
* **Solution**: Install the missing dependency using `npm install` or `yarn add`.

### `Error: Invalid configuration...`

* **Cause**: Issues with the Astro configuration file.
* **Solution**:
    * Check for syntax errors or typos.
    * Ensure correct option names and values.
    * Refer to the Astro documentation for configuration guidelines.

### Content Processing Errors

* **Markdown/MDX syntax errors**:
    * **Cause**: Invalid Markdown or MDX syntax in content files.
    * **Solution**: Review and correct the syntax errors in the affected files.
* **Unsupported features**:
    * **Cause**: Using Markdown/MDX features not supported by the current setup.
    * **Solution**:
        * Check the documentation for supported features.
        * Consider using plugins or custom components for additional functionality.

## Runtime Issues (Client-Side)

### 404 Not Found Errors

* **Cause**: Requested page or asset does not exist.
* **Solution**:
    * Verify the URL for typos.
    * Ensure the content file is in the correct location and properly linked.

### JavaScript Errors

* **Cause**: Errors in client-side JavaScript code.
* **Solution**:
    * Check the browser console for error messages and stack traces.
    * Debug the JavaScript code to identify and fix the issue.

### Styling Issues

* **Missing or incorrect Tailwind CSS classes**:
    * **Cause**: Typos or incorrect class names used in components.
    * **Solution**: Verify the class names against the Tailwind CSS documentation.
* **Conflicting styles**:
    * **Cause**: Custom CSS or other stylesheets overriding Tailwind styles.
    * **Solution**:
        * Review the CSS specificity rules.
        * Adjust the order of stylesheets or use more specific selectors.

## General Tips

* **Clear Cache and Hard Reload**: If you encounter unexpected behavior after making changes, try clearing your browser cache and performing a hard reload (Ctrl+Shift+R or Cmd+Shift+R). 
* **Check Documentation and Resources**: Refer to the Astro, Starlight, and Tailwind CSS documentation for detailed information and troubleshooting guidance. 
* **Community Support**: Seek assistance from the Astro Discord community or online forums for help with specific issues. 
