---
title: Gemi-Doc Component Interactions
description: A visual representation of how the various components within Gemi-Doc communicate and exchange data.
---

# Interaction Diagram

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

## Interaction Flows

1. **Content Processing:**
   - Astro framework reads Markdown/MDX content files.
   - Starlight integration provides content collection and processing capabilities.
   - Markdown/MDX processors (e.g., `remark`, `rehype`) handle syntax highlighting, rendering, and other transformations.
   - Processed content is passed back to the Astro framework.

2. **Styling:**
   - Astro framework applies Tailwind CSS styles to the processed content.
   - Users can optionally add custom CSS for further styling modifications.
   - Styled content is generated as HTML.

3. **Build Process:**
   - Astro framework generates static HTML files for the entire documentation site. 
   - These static files are ready to be served from a web server or CDN. 
