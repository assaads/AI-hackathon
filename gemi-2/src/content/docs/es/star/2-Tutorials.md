---
title: Tutoriales del proyecto Starlight
description: Guías paso a paso para utilizar eficazmente las características del proyecto Starlight.
---

## Tutorial 1: Creación y edición de contenido

Este tutorial te guiará a través del proceso de creación y edición de contenido dentro de tu proyecto Starlight.

### Paso 1: Acceder a los archivos de contenido

Navega al directorio `src/content/`. Aquí encontrarás archivos Markdown o MDX que contienen el contenido de tu sitio web.

### Paso 2: Modificar contenido existente

1.  Elige el archivo Markdown o MDX que deseas editar.
2.  Abre el archivo utilizando tu editor de texto o IDE preferido.
3.  Realiza los cambios necesarios al contenido.
4.  Guarda el archivo. El servidor de desarrollo actualizará automáticamente el sitio para reflejar tus ediciones.

### Paso 3: Crear nuevo contenido

1.  Crea un nuevo archivo Markdown o MDX dentro del directorio `src/content/`.
2.  Agrega frontmatter al principio del archivo para definir atributos como el título y la descripción:

```markdown
---
title: Mi nueva página
description: Esta es una nueva página en mi sitio Starlight.
---
```

3.  Escribe tu contenido en formato Markdown o MDX debajo del frontmatter.
4.  Guarda el archivo. Tu nueva página ahora será accesible en tu sitio Starlight.

## Tutorial 2: Personalizar los metadatos del sitio

Este tutorial demuestra cómo personalizar los metadatos de tu sitio Starlight, incluyendo el título y la descripción.

### Paso 1: Abrir el archivo de configuración

Localiza y abre el archivo `astro.config.mjs` en el directorio raíz de tu proyecto.

### Paso 2: Editar los metadatos del sitio

Dentro del archivo `astro.config.mjs`, encuentra la propiedad `site`. Esta propiedad te permite definir varios atributos de metadatos:

```javascript
export default defineConfig({
  // ... other configuration options
  site: 'https://example.com', // Replace with your domain
  markdown: {
    shikiConfig: {
      theme: 'dracula',
    },
  },
});
```

Modifica los campos `title` y `description` a los valores deseados:

```javascript
export default defineConfig({
  // ... other configuration options
  site: 'https://example.com', // Replace with your domain
  markdown: {
    shikiConfig: {
      theme: 'dracula',
    },
  },
});
```

### Paso 3: Guardar cambios

Guarda el archivo `astro.config.mjs`. Los metadatos actualizados se reflejarán en tu sitio Starlight.

## Tutorial 3: Agregar una barra lateral

Este tutorial te guiará a través del proceso de incorporar una barra lateral a tu proyecto Starlight para mejorar la navegación.

### Paso 1: Definir la configuración de la barra lateral

Abre el archivo `astro.config.mjs` y localiza la propiedad `starlight` dentro del objeto de configuración.

### Paso 2: Configurar los elementos de la barra lateral

Dentro de la propiedad `starlight`, encontrarás la opción `sidebar`. Esta opción te permite definir una matriz de objetos, donde cada objeto representa una sección o página en tu barra lateral:

```javascript
// ... other configuration options
starlight({
  // ... other Starlight options
  sidebar: [
    {
      title: 'Sección 1',
      items: [
        { title: 'Página 1', link: '/page-1' },
        { title: 'Página 2', link: '/page-2' },
      ],
    },
    {
      title: 'Sección 2',
      items: [
        // ... page links for section 2
      ],
    },
  ],
}),
```

Personaliza las propiedades `title` y `link` de cada elemento para que coincidan con la estructura de tu contenido.

### Paso 3: Guardar y previsualizar

Guarda el archivo `astro.config.mjs`. Tu sitio Starlight ahora mostrará la barra lateral configurada, proporcionando una mejor navegación para tus usuarios. 
