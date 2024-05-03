```
[Content Layer]
    |
    +-- [Markdown/MDX Files]
    |   |
    |   +-- index.mdx 
    |   +-- guides/
    |       +-- example.md
    |   +-- reference/
    |       +-- example.md
    |   +-- my-tries/
    |       +-- openaiService.md
    |
    +-- [Content Configuration (config.ts)]
         |
         +-- defineCollection()

[Presentation Layer]
    |
    +-- [Components]
    |   |
    |   +-- Card
    |   +-- CardGrid
    |
    +-- [Pages]
    |   |
    |   +-- index.astro
    |
    +-- [Layouts]
         |
         +-- SplashLayout.astro

[Styling Layer]
    |
    +-- [Tailwind CSS (tailwind.config.mjs)]
         |
         +-- theme
         +-- plugins

[Build Tooling]
    |
    +-- [Astro (astro.config.mjs)]
         |
         +-- markdownOptions
         +-- starlightConfig

[External Dependencies]
    |
    +-- openai (npm package)
    +-- axios (npm package)
    +-- @astrojs/starlight (npm package)

```