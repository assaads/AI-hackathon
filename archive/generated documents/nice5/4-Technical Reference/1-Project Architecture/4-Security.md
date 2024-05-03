---
title: Gemi-Doc Security Considerations
description: Understanding potential security aspects when deploying and using Gemi-Doc for your documentation site. 
---

# Security Considerations

Since Gemi-Doc generates static HTML files, it inherently minimizes certain security risks associated with dynamic web applications. There is no server-side execution or database involved, reducing the attack surface. However, some security aspects still need to be considered:

## Web Server and Hosting Security

- **Secure Web Server Configuration:** Ensure your web server or hosting platform is configured with security best practices, such as keeping software updated, using strong passwords, and implementing appropriate access controls. 
- **HTTPS:** Use HTTPS to encrypt communication between the server and clients, protecting sensitive information.

## Content Security

- **Content Validation:** Be cautious when including content from external sources or user-generated content to prevent cross-site scripting (XSS) vulnerabilities.
- **Sensitive Information:** Avoid storing sensitive information directly within your documentation content.

## Build Process Security

- **Dependency Management:** Keep dependencies up-to-date to address known vulnerabilities.
- **Build Environment:** Ensure the security of your build environment, including the operating system and any tools used in the build process. 

## Additional Considerations

- **Authentication and Authorization:** If your documentation requires access control, consider implementing authentication and authorization mechanisms at the web server or CDN level. 
- **Regular Security Audits:** Periodically review your documentation site and infrastructure for potential security risks. 
