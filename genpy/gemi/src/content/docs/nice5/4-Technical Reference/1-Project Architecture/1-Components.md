---
title: Gemi-Doc Architecture
description: An overview of the main components and their interactions within the Gemi-Doc documentation site generator.
--- 

# Component Diagram

```
+----------------+    +-----------------+    +----------------+
|   Astro       |    |   Starlight     |    |    Content     |
|   Framework   |    |  Integration   |    |    (MD/MDX)    |
+----------------+    +-----------------+    +----------------+
        ^                   ^                   ^
        |                   |                   |
+----------------+    +-----------------+    +----------------+
|   Tailwind CSS |    |  Markdown/MDX  |    |  Custom CSS   | 
|   (Styling)   |    |  (Processing)   |    |    (Optional)  |
+----------------+    +-----------------+    +----------------+
```

## Component Descriptions 

- **Astro Framework:** The underlying static site generator that provides the foundation for building the documentation site. 
- **Starlight Integration:** An Astro integration that adds features specifically for creating documentation sites, such as content collections, sidebar navigation, and search functionality.
- **Content (MD/MDX):** The actual documentation content written in Markdown or MDX format. 
- **Tailwind CSS:** A utility-first CSS framework used for styling the documentation site. 
- **Markdown/MDX Processing:** Tools like `remark` and `rehype` are utilized to process Markdown and MDX content, including syntax highlighting and rendering. 
- **Custom CSS (Optional):** Users have the option to add custom CSS styles to personalize the appearance of the documentation site beyond the default Tailwind CSS styles. 
