---
title: Starlight Documentation Site Function and Method Documentation
description: Guidance on documenting functions and methods within a Starlight documentation site context, considering its static nature and content-centric approach.
---

# Function & Method Documentation

Starlight documentation sites, built with Astro's static site generation, typically involve a different approach to function and method documentation compared to traditional codebases with extensive server-side logic or complex client-side interactions.

## Considerations

* **Static Site Nature**: Starlight documentation sites primarily focus on delivering content through static HTML pages generated from Markdown or MDX files. While JavaScript may be used for interactive elements or client-side logic, it is not the central aspect of the site's functionality.
* **Content-Centric Approach**: The primary goal is to present information and guides to users effectively, rather than providing in-depth documentation of code implementation details.
* **Alternative Strategies**: If your project involves significant JavaScript code with numerous functions and methods, consider alternative documentation methods: 
    * **JSDoc**: Use JSDoc comments within your JavaScript code to provide detailed documentation for functions, methods, and their parameters. 
    * **Code Snippets and Explanations**: Include relevant code snippets and explanations within your Markdown/MDX content to provide context and clarity where necessary. 
    * **Comments and Docstrings**: Utilize clear and concise comments and docstrings within your JavaScript code to explain the purpose and behavior of functions and methods for developers working with the codebase directly. 

## Recommendations

* Assess the complexity and scope of your JavaScript code to determine if dedicated function and method documentation is required.
* Choose a documentation approach that aligns with your project's structure and the needs of your target audience.
* Strive for clarity and conciseness in your documentation, ensuring it is easily understandable and accessible to users who require it. 
* Maintain consistency in your documentation style and format throughout the project. 
