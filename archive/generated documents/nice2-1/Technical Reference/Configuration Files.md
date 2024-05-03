---
title: Configuration Files - Starlight Documentation Site
description: An overview of the key configuration files and options used to customize the Starlight documentation site project.
---

# Configuration Files

The Starlight documentation site project utilizes several configuration files to manage dependencies, customize the build process, and define the structure and behavior of the site. 

## `package.json`

This file stores project metadata and manages dependencies:

*   **`name`:** The name of your project.
*   **`version`:** The current version of your project.
*   **`scripts`:** Defines scripts for development tasks:
    *   `dev`: Starts the Astro development server.
    *   `build`: Builds the project for production.
    *   **`preview`:** Previews the production build locally.
*   **`dependencies`:** Lists the required packages for the project, including Astro, Starlight, and Tailwind CSS.
*   **`devDependencies`:** (Optional) Lists development-specific dependencies, such as testing or linting tools. 

## `astro.config.mjs`

This file configures the Astro project and integrates plugins like Starlight:

*   **`integrations`:** An array that includes plugins to extend Astro's functionality:
    *   **`starlight()`:** Configures the Starlight plugin:
        *   **`title`:** Sets the title of your documentation site.
        *   **`logo`:** (Optional) Specifies a logo image for the site.
        *   **`sidebar`:** Defines the structure and content of the sidebar navigation. See the "How-To Guides" section for details on customizing the sidebar. 
        *   **`social`:** (Optional) Provides links to your social media profiles. 
    *   **`tailwind()`:** Integrates Tailwind CSS into the project. 

## `tailwind.config.js` (or `.mjs`)

This file customizes the Tailwind CSS configuration:

*   **`content`:** Specifies the files that Tailwind should scan for class names. This ensures that only the necessary styles are included in the final CSS output. 
*   **`theme`:** Allows you to customize the Tailwind theme, including colors, fonts, spacing, and more. 
*   **`plugins`:** Enables you to add third-party Tailwind plugins to extend its functionality. 

## `tsconfig.json`

This file configures the TypeScript compiler:

*   **`extends`:** Inherits settings from Astro's recommended TypeScript configuration.
*   **Compiler options:** (Optional) You can add or modify compiler options to customize TypeScript behavior.

## Conclusion

Understanding the configuration files and options within the Starlight documentation site project empowers you to tailor the build process, site structure, and appearance to meet your specific requirements. Refer to the documentation for each tool (Astro, Starlight, Tailwind CSS, TypeScript) for more detailed information on available configuration options. 

