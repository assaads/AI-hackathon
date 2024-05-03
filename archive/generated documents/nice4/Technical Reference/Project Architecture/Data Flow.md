---
title: Data Flow in Starlight Docs
description: A visual representation of how data moves through the Starlight documentation system. 
---

# Data Flow in Starlight Docs

## Content Retrieval and Processing

```
[MD/MDX Files] ---> [Astro Build Process] ---> [HTML]

```

1. **Content Source:** Markdown (`.md`) and MDX (`.mdx`) files stored in the `src/content/docs/` directory serve as the primary source of data.

2. **Astro Build Process:**
   - Astro's build process parses the MD/MDX files, extracting content and frontmatter. 
   - Frontmatter data is used to define page metadata, such as titles, descriptions, and template layouts.
   - Markdown/MDX content is transformed into HTML, incorporating any JSX components or custom styling as defined.

3. **HTML Generation:** The build process generates static HTML files, which represent the final documentation pages.

## Data Persistence

- **Static Site Generation:** Starlight, as a static site generator, does not inherently involve a database or server-side data persistence. 
- **Content Updates:** Modifications to the documentation require updating the source MD/MDX files and rebuilding the site to regenerate the static HTML files. 


## Optional Data Flows

### 1. Search Indexing 

- If a search engine like Pagefind is integrated, an additional data flow involves indexing the content of the generated HTML files to enable search functionality. 

### 2. OpenAI API Interaction

- The `OpenAIService` class can introduce a data flow where user prompts are sent to the OpenAI API and the resulting generated text is received and potentially incorporated into the documentation. 


## Conclusion 

The data flow in a Starlight documentation system primarily involves the transformation of MD/MDX content into static HTML pages during the build process. Optional integrations like search and OpenAI can introduce additional data flows for enhanced functionality. 
