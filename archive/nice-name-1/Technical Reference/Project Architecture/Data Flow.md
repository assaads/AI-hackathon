---
title: Starlight Documentation Site Data Flow
description: A representation of how data moves through the different components of a Starlight documentation site.
---

# Data Flow

## Content Processing and Rendering 

```
+-----------------+    +-----------------+    +-----------------+
|     Content     |    |   Starlight    |    |     Astro       |
| (Markdown/MDX) |    |                 |    |                 |
+--------+--------+    | (Theme, Layout,|    | (Static Site    |
         |             |   Features)     |    |  Generator)     |
         +--------->   +--------+--------+    +--------+--------+
                   Content Data            Processed Data          |
                                                                   v
                                                      +-----------------+
                                                      |  Generated HTML | 
                                                      |     Pages      |
                                                      +-----------------+ 
```

1. **Content Source**: Markdown or MDX files containing the raw documentation content serve as the initial data source. 
2. **Starlight Processing**: Starlight ingests the content data and applies the specified theme, layout, and any additional features. This step transforms the raw content into a structured format suitable for Astro's rendering process. 
3. **Astro Rendering**: Astro receives the processed content data from Starlight and generates the final HTML pages for each documentation page. This involves combining the content with the layout template and incorporating any necessary assets or components.
4. **HTML Output**: The generated HTML pages represent the final form of the data, ready to be delivered to users' web browsers. 

## Additional Data Flows (Optional)

* **API Interactions**: If your documentation site interacts with external APIs or services, indicate the flow of requests and responses between the site and the external entities.
* **Database Access**: For sites that utilize a database, illustrate how data is retrieved from or stored in the database during the content processing or rendering phases.
* **User Input**: If your documentation site allows for user input or interaction, depict the flow of user-generated data through the system.

## Customization 

Adapt these diagrams to accurately represent the data flow within your specific Starlight documentation site project, considering any unique integrations or data dependencies. 
