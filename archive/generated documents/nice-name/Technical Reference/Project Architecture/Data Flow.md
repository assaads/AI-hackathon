---
title: Data Flow 
description: Illustration of how data flows through the various components of the Starlight documentation site. 
---

# Data Flow Diagram

```
+----------------+    +--------------+    +---------------+    +--------------+
|    Content     |    |   Starlight  |    |     Astro     |    |   Pagefind   |
|  (Markdown/    |    |  Integration |    |   Framework   |    |  (Search)   | 
|      MDX)     |--->|    (Plugin)   |--->|   (Renderer)  |--->|              |
+----------------+    +--------------+    +---------------+    +--------------+
       |               |                   |                   |
       |               |                   |                   |  
       v               v                   v                   v 
  +-----------+   +-----------+   +------------+    +-------------+
  | Frontmatter |   |  Content   |   |  HTML Pages |    | Search Index |
  |  (Metadata) |   |   (Text)  |   |   (Output)  |--->|   (Database) |
  +-----------+   +-----------+   +------------+    +-------------+ 
                                                ^       |
                                                |       |
                                                |       |
                                         +--------------+    +--------------+
                                         |     User     |    |   Browser    |
                                         |   (Input)   |--->|  (Output)   |
                                         +--------------+    +--------------+
```

## Data Flow Description 

1. **Content Creation:** Authors write documentation in Markdown or MDX format, including frontmatter with metadata (title, description, etc.) and the main content.
2. **Content Processing:** The Starlight plugin parses the Markdown/MDX files, extracting the frontmatter and content.
3. **Content Transformation:** Astro renders the content into HTML pages, applying styling and layout.
4. **Search Indexing:** Pagefind processes the rendered HTML pages and creates a search index, storing relevant information for efficient search queries.
5. **User Interaction:** Users access the documentation site through their browsers. They can navigate through pages or utilize the search functionality.
6. **Search Query Processing:** When a user performs a search, Pagefind utilizes the search index to retrieve relevant results based on the user's query.
7. **Content Delivery:** The requested HTML pages, including search results, are delivered to the user's browser for display.

## Data Lifecycle Summary

*   Data originates as Markdown/MDX content with frontmatter metadata.
*   Starlight and Astro process and transform the data into HTML pages.
*   Pagefind indexes the data for search functionality.
*   Users interact with the data through navigation and search queries.
*   The processed and retrieved data is ultimately displayed in the user's browser. 
