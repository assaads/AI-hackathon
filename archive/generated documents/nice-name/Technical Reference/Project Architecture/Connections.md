---
title: Connections 
description: Illustration of how the main components interact within the Starlight documentation site architecture.
---

# Data Flow Diagram

```
+----------------+    +--------------+    +---------------+    +--------------+
|    Content     |    |   Starlight  |    |     Astro     |    |   Pagefind   |
|  (Markdown/    |    |  Integration |    |   Framework   |    |  (Search)   | 
|      MDX)     |--->|    (Plugin)   |--->|   (Renderer)  |--->|              |
+----------------+    +--------------+    +---------------+    +--------------+
                   ^                   |                   ^ 
                   |                   |                   |
                   |                   v                   |
            +--------------+    +------------+    +--------------+
            |     User     |    |   Tailwind  |    |   Browser    |
            |   (Input)   |<---|   (Styling) |<---|  (Output)   |
            +--------------+    +------------+    +--------------+
```

## Interaction Descriptions

*   **Content to Starlight:** Markdown/MDX files are read and processed by the Starlight plugin.
*   **Starlight to Astro:** Starlight prepares the content and interacts with Astro to render the HTML pages.
*   **Astro to Pagefind:** The rendered HTML content is passed to Pagefind for indexing and enabling search capabilities.
*   **Tailwind to Astro/Starlight:** Tailwind CSS classes are applied to the content during the rendering process, providing styling and visual presentation.
*   **User to Astro/Starlight:** Users interact with the site through the browser, triggering page navigation and search queries.
*   **Astro/Starlight to Browser:** The rendered HTML pages, including the styled content and search results, are delivered to the user's browser for display. 

# Additional Interactions

*   **Third-party Integrations:**  Interactions with external APIs or services may occur depending on the specific integrations used. 
*   **Custom Components:** Custom components might communicate with each other or with external data sources through API calls or events. 
*   **Data Sources:** If your site relies on external data, there will be interactions between the site and the data sources (e.g., API requests and responses). 
