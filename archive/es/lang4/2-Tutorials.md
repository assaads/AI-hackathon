---
title: Tutoriales de Documentación de Starlight
description: Guías paso a paso para utilizar eficazmente las características de Starlight para construir su sitio de documentación.
---

## Creando y Editando Páginas de Documentación

Starlight utiliza principalmente archivos Markdown (`.md`) o MDX (`.mdx`) para crear páginas de documentación. Estos archivos deben colocarse dentro del directorio `src/content/docs/`. El nombre del archivo determina la ruta de la URL para cada página. 

### Creando una Nueva Página

1.  **Crear un nuevo archivo**: Dentro del directorio `src/content/docs/`, cree un nuevo archivo con un nombre descriptivo utilizando la extensión `.md` o `.mdx`. Por ejemplo, `nueva-caracteristica.md`.
2.  **Agregar contenido**: Escriba el contenido de su documentación utilizando la sintaxis de Markdown. Puede incluir encabezados, párrafos, bloques de código, imágenes y otros elementos de Markdown.

### Editando una Página Existente

1.  **Localizar el archivo**: Encuentre el archivo Markdown o MDX que desea editar dentro del directorio `src/content/docs/`. 
2.  **Hacer cambios**: Abra el archivo en un editor de texto y modifique el contenido según sea necesario.

## Estructurando su Documentación

Starlight ofrece flexibilidad para organizar su documentación utilizando carpetas dentro del directorio `src/content/docs/`. Esto le permite crear una estructura jerárquica para su contenido.

### Creando Secciones

1.  **Crear una carpeta**: Dentro del directorio `src/content/docs/`, cree una nueva carpeta para cada sección de su documentación. Por ejemplo, `guias/` o `referencia/`.
2.  **Agregar páginas**: Dentro de cada carpeta de sección, cree archivos Markdown o MDX para las páginas individuales dentro de esa sección.

## Agregando Imágenes

Mejore su documentación con imágenes colocándolas en el directorio `src/assets/` y referenciándolas dentro de su contenido Markdown.

### Incrustando una Imagen

```markdown
![Descripción de la imagen](../assets/imagen.png)
```

## Opciones de Configuración

Explore el archivo `astro.config.mjs` para personalizar varios aspectos de su sitio de documentación de Starlight. Consulte la Guía de configuración del proyecto Starlight para obtener información detallada sobre las opciones disponibles. 
