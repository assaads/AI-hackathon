---
title: Troubleshooting Guide
description: Solutions to common issues encountered while working with the Starlight project.
---

## Common Issues

### Development Server Not Starting

*   **Problem:** When you run `npm run dev` or `yarn dev`, the development server fails to start or throws errors.
*   **Possible Causes:**
    *   Port conflict: Another application might be using the same port (default is 3000).
    *   Missing dependencies: Required dependencies might not be installed correctly.
    *   Configuration errors: There might be errors in your `astro.config.mjs` file. 
*   **Solutions:**
    *   Change the port: Modify the port number in the `astro.config.mjs` file or use the `--port` flag when starting the server.
    *   Reinstall dependencies: Run `npm install` or `yarn install` to ensure all dependencies are installed. 
    *   Check configuration: Review your `astro.config.mjs` file for any syntax errors or incorrect settings.

### Content Changes Not Reflecting

*   **Problem:** After making changes to your Markdown or MDX content files, the updates are not reflected on the development site.
*   **Possible Causes:**
    *   Caching issues: The browser or development server might be caching old content.
    *   Incorrect file paths: You might be editing the wrong files or have incorrect file paths in your configuration. 
*   **Solutions:**
    *   Clear cache: Clear your browser cache or restart the development server to force a reload.
    *   Verify file paths: Ensure that you are editing the correct content files and that the file paths in your `astro.config.mjs` file are accurate. 

### Styling Issues

*   **Problem:** Your Starlight site is not displaying styles correctly, or the Tailwind CSS classes are not being applied.
*   **Possible Causes:**
    *   Tailwind CSS configuration: There might be errors in your `tailwind.config.mjs` file.
    *   Missing Tailwind directives: You might have forgotten to include the necessary Tailwind directives in your layout or page components. 
*   **Solutions:**
    *   Check Tailwind configuration: Review your `tailwind.config.mjs` file and ensure that the content paths and other settings are correct.
    *   Add Tailwind directives: Make sure you have added the `@tailwind` directives for base, components, and utilities in your layout or page components where you want to use Tailwind classes. 

### OpenAI API Errors

*   **Problem:** You are encountering errors when using the OpenAI API integration.
*   **Possible Causes:** See the dedicated section on "Error Codes and Messages" for detailed explanations and solutions for common OpenAI API errors.

## Additional Tips

*   **Consult Documentation:** Refer to the official [Starlight documentation](https://starlight.astro.build/) and the [Astro documentation](https://docs.astro.build/) for in-depth information and troubleshooting guidance. 
*   **Community Support:** Seek help from the Starlight and Astro communities, where you can find answers to common questions and get assistance from experienced users.
*   **Debugging Tools:** Utilize browser developer tools and debugging techniques to identify and resolve issues effectively. 


