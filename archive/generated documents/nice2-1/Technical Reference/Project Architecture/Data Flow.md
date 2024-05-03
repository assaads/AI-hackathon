---
title: Data Flow - Starlight Documentation Site
description: Tracing the movement of data throughout the various stages of the Starlight documentation site's lifecycle.
---

# Data Flow

## Content Creation and Processing

```
+-----------------+    +-----------------+    +---------+    +---------+
| Markdown/MDX    |--->|   Astro        |--->| Components  |--->|  Layouts  |
+-----------------+    +-----------------+    +---------+    +---------+
                                                    |
                                                    v
                                           +-----------------+
                                           |    Static HTML   |
                                           +-----------------+
```

1.  **Content Authoring:** Authors create and edit Markdown or MDX files, which serve as the primary source of data (content) for the documentation site.
2.  **Astro Processing:** Astro parses the Markdown/MDX files and converts them into HTML, representing the processed and structured content.
3.  **Component Integration:** Reusable components are incorporated into the HTML structure, potentially introducing dynamic data or state.
4.  **Layout Application:** Layout templates are applied to the HTML, providing the overall page structure and potentially injecting additional data.
5.  **Static HTML Generation:** Astro generates static HTML files, which encapsulate the final content and structure of the documentation pages.

## Content Delivery

```
+-----------------+    +-----------------+
|   Static HTML   |--->|   Content CDN   |---> User (Browser)
+-----------------+    +-----------------+ 
```

1.  **Static File Storage:** The generated static HTML files are stored on a hosting platform or file storage service.
2.  **Content Delivery Network (CDN):**  A CDN caches the static HTML files at edge locations closer to users, optimizing delivery speed and performance.
3.  **User Access:** Users request and receive the static HTML files from the CDN or directly from the hosting platform, accessing the documentation content in their web browsers. 

## Conclusion

The data flow in a Starlight documentation site follows a linear path, starting with content creation, progressing through processing and structuring, and culminating in the delivery of static HTML files to users. The CDN plays a crucial role in optimizing content delivery and enhancing user experience. 
