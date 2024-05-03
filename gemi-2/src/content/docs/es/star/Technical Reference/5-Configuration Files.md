---
title: Archivos de configuración: astro.config.mjs
description: Una guía para configurar tu proyecto Starlight utilizando el archivo astro.config.mjs.
---

## astro.config.mjs

El archivo `astro.config.mjs` sirve como el centro neurálgico para configurar varios aspectos de tu proyecto Starlight. Te permite definir metadatos del sitio, integrar herramientas externas, personalizar la configuración de compilación y más.

### Metadatos del sitio

*   **site**: (string) Especifica la URL base de tu sitio web. Esto es esencial para generar URL correctas para enlaces internos y activos.

```javascript
export default defineConfig({
  // ... other configuration options
  site: 'https://example.com', // Reemplaza con tu dominio
});
```

### Opciones de contenido

*   **markdown**: (object) Configura opciones relacionadas con el procesamiento de Markdown.
    *   **shikiConfig**: (object) Permite la personalización del resaltado de código utilizando la biblioteca Shiki. Puedes especificar el tema deseado y otras opciones.

```javascript
export default defineConfig({
  // ... other configuration options
  markdown: {
    shikiConfig: {
      theme: 'dracula', // Establece el tema de resaltado de código
    },
  },
});
```

### Opciones de Starlight

*   **starlight()**: Una función que acepta un objeto de opciones para configurar ajustes específicos de Starlight.
    *   **sidebar**: (array) Define la estructura y el contenido de la navegación de la barra lateral. Cada elemento de la matriz representa una sección o página, con propiedades como `title` y `link`.

```javascript
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  // ... other configuration options
  integrations: [starlight({
    // ... other Starlight options
    sidebar: [
      {
        title: 'Sección 1',
        items: [
          { title: 'Página 1', link: '/page-1' },
          { title: 'Página 2', link: '/page-2' },
        ],
      },
      // ... more sidebar sections
    ],
  })],
});
```

## Opciones de configuración adicionales

El archivo `astro.config.mjs` ofrece muchas otras opciones de configuración para adaptar tu proyecto a tus necesidades específicas. Consulta la [documentación oficial de Astro](https://docs.astro.build/en/reference/configuration-reference/) para obtener una lista completa y explicaciones detalladas. 


