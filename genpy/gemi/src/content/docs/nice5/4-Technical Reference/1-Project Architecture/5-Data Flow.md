---
title: Gemi-Doc Data Flow
description: A visual representation of how data is processed and transformed within the Gemi-Doc system.
---

# Data Flow Diagram

```
+----------------+    +-----------------+    +----------------+
|   Content     |    |  Markdown/MDX  |    |   Astro       | 
|   (MD/MDX)    |---> |  (Processing)   |---> |   Framework   | 
+----------------+    +-----------------+    +----------------+
                               ^
                               |
                         +----------------+
                         |   Tailwind CSS |
                         |   (Styling)   | 
                         +----------------+
```

## Data Flow Steps

1. **Content Input:**
   - Markdown (MD) or MDX files serve as the primary data source for the documentation content.

2. **Content Processing:**
   - The Markdown/MDX processor parses the content files.
   - It applies syntax highlighting, converts MDX to HTML with embedded JSX components, and performs other necessary transformations.

3. **Content Transformation:**
   - The processed content is passed to the Astro framework. 
   - Astro combines the content with layouts and applies Tailwind CSS styles.

4. **Static Site Generation:**
   - Astro generates static HTML files, which represent the final output of the data flow process. 
   - These HTML files contain the styled and processed content, ready to be served to users. 
