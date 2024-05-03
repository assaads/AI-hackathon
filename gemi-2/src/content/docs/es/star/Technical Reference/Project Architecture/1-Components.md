```
[Capa de contenido]
    |
    +-- [Archivos Markdown/MDX]
    |   |
    |   +-- index.mdx
    |   +-- guides/
    |       +-- example.md
    |   +-- reference/
    |       +-- example.md
    |   +-- my-tries/
    |       +-- openaiService.md
    |
    +-- [Configuración de contenido (config.ts)]
         |
         +-- defineCollection()

[Capa de presentación]
    |
    +-- [Componentes]
    |   |
    |   +-- Card
    |   +-- CardGrid
    |
    +-- [Páginas]
    |   |
    |   +-- index.astro
    |
    +-- [Diseños]
         |
         +-- SplashLayout.astro

[Capa de estilos]
    |
    +-- [Tailwind CSS (tailwind.config.mjs)]
         |
         +-- theme
         +-- plugins

[Herramientas de construcción]
    |
    +-- [Astro (astro.config.mjs)]
         |
         +-- markdownOptions
         +-- starlightConfig

[Dependencias externas]
    |
    +-- openai (paquete npm)
    +-- axios (paquete npm)
    +-- @astrojs/starlight (paquete npm)

```
