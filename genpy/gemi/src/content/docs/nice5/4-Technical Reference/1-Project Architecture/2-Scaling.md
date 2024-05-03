---
title: Scaling Gemi-Doc
description: Strategies for scaling your Gemi-Doc documentation site to accommodate increased traffic and content volume.
--- 

# Scaling Strategies

Gemi-Doc, as a static site generator, inherently possesses good scalability characteristics. The generated HTML files can be served directly from a content delivery network (CDN), enabling efficient distribution and handling of high traffic volumes. 

## Horizontal Scaling

Horizontal scaling involves adding more instances of components to distribute the load. In the context of Gemi-Doc, this primarily applies to the web server or hosting platform serving the static files. 

```
    +----------+       +----------+       +----------+
    | Web Server | ----> | Web Server | ----> | Web Server | 
    +----------+       +----------+       +----------+ 
           ^                   ^                   ^
           |                   |                   |
    +-------------------------------------------------+
    |                     CDN                       | 
    +-------------------------------------------------+
```

By adding more web server instances behind a CDN, incoming requests can be distributed across multiple servers, preventing any single server from becoming overloaded. 

## Vertical Scaling

Vertical scaling involves increasing the resources (e.g., CPU, RAM) of individual components. For Gemi-Doc, this could be applicable to the build process, especially for large documentation sites with extensive content and complex processing requirements. 

```
+---------------------+
|      Build Server   |
|  (Increased Resources)  |
+---------------------+
        |
        v
+---------------------+
|    Static Files    |
|   (HTML, CSS, JS)   |
+---------------------+
        |
        v 
+---------------------+
|        CDN         |
+---------------------+ 
```

By providing the build server with more resources, the build process can be expedited, resulting in faster generation of static files. 
