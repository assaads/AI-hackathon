```
[User]
   |
   | HTTP Request
   V
[Astro (Build Tooling)] --> [Content Layer (Markdown/MDX Files)] --> [Astro (Build Tooling)]
   |                                 ^                                      |
   |                                 | Content Processing                   |
   |                                 | (Markdown parsing, etc.)            |
   +-- Generates HTML pages ---------+

``` 
