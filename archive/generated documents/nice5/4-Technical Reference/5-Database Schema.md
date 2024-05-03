---
title: Gemi-Doc Database Schema 
description: Information regarding the database structure used in Gemi-Doc projects, including tables, columns, data types, and relationships.
---

# Database Usage in Gemi-Doc

## Introduction

Gemi-Doc, as a static site generator, does not inherently utilize or require a database. The content for the documentation site is stored in Markdown (MD) or MDX files within the project's directory structure. This approach offers several advantages:

- **Simplicity:** Managing content in files is straightforward and does not require setting up or maintaining a database.
- **Version Control:** Documentation content can be easily version-controlled using Git or other version control systems, enabling tracking changes and collaboration. 
- **Portability:** The documentation content is self-contained within the project, making it easy to move or deploy the site to different environments.

## Potential Use Cases for a Database

While Gemi-Doc itself does not use a database, there might be scenarios where a database could be integrated into a documentation project:

- **Dynamic Content:** If your documentation requires displaying dynamic content, such as user comments, ratings, or personalized information, a database could be used to store and retrieve this data. 
- **Content Management System (CMS):** For larger documentation projects with multiple authors and complex workflows, a CMS could be employed to manage content creation and editing. A CMS typically relies on a database to store content and associated metadata.

## Conclusion

Gemi-Doc's file-based approach to content management provides simplicity and flexibility for building documentation sites. However, depending on your specific requirements, integrating a database could be a viable option for handling dynamic content or implementing a CMS. 
