---
title: Starlight Documentation Project: Data Flow 
description: Illustrating data flow within the Starlight documentation project using ASCII diagrams.
---

## Data Flow during Build Process

```
+-----------------------+    +-------------------+    +-------------------+
| Documentation Content | -> | Markdown/MDX      | -> |   Astro           |
|    (MD/MDX files)    |    |   Processing      |    |   Components      |
+-----------------------+    +-------------------+    +-------------------+
                                       ^                   ^
                                       |                   | 
                                       |    +-------------------+    +-------------------+
                                       +--- |  Starlight Plugin  |    |  Tailwind CSS     |
                                            +-------------------+    +-------------------+
                                                                         ^
                                                                         |
                                                        +---------------------------------+
                                                        |         Output Directory         | 
                                                        |       (HTML and static assets)   |
                                                        +---------------------------------+ 
```

1. **Documentation Content**: The data originates from the Markdown (MD) or MDX files containing the documentation content, located in the `src/content/` directory. 
2. **Markdown/MDX Processing**: The content files undergo processing, where the Markdown or MDX syntax is parsed and converted into HTML. This stage may also involve enhancements from Starlight or custom components.
3. **Astro Components**: Astro components, including those provided by the Starlight plugin, are used to structure and style the processed HTML content. Data, such as text, code, and images, flows through these components to create the final presentation. 
4. **Output Directory**: The resulting HTML files, along with any static assets (images, stylesheets, etc.), are placed in the designated output directory, typically `dist/`, ready for deployment.

## Data Flow at Runtime

```
+-------------------+    +---------------------------------+
|   Web Browser     | -> |       Static Web Host         |
+-------------------+    +---------------------------------+
                                       ^
                                       |
                                       |
                                +-------+-------+
                                | HTML Files    |
                                | Static Assets |
                                +-------+-------+
``` 

1. **Web Browser**: When a user accesses the documentation site, the web browser sends requests to the static web host.
2. **Static Web Host**: The web host responds by serving the pre-rendered HTML files and static assets directly to the browser. There is no further data processing or dynamic content generation involved at this stage. 
