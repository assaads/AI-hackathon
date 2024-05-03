---
title: Primeros Pasos con el Proyecto de Documentación Starlight
description: Una guía completa para instalar, configurar y comenzar a usar Starlight para sus necesidades de documentación.
---

## Prerrequisitos

Antes de comenzar el proceso de configuración, asegúrese de tener instalados los siguientes requisitos previos en su sistema:

*   **Node.js**: Descargue e instale la última versión LTS de Node.js desde el sitio web oficial (https://nodejs.org/).

## Instalación

1.  **Crear un nuevo proyecto**: Abra su terminal y ejecute el siguiente comando:

```bash
npm create astro@latest mi-proyecto-docs -- --template starlight
```

Este comando utiliza la CLI de Astro para crear un nuevo directorio de proyecto llamado `mi-proyecto-docs` y lo inicializa con la plantilla de Starlight.

2.  **Navegar al directorio del proyecto**:

```bash
cd mi-proyecto-docs
```

3.  **Instalar dependencias**:

```bash
npm install
```

Este comando instala todas las dependencias necesarias para que el proyecto Starlight funcione correctamente. 

## Estructura del Proyecto

Una vez que se complete la instalación, familiarícese con la estructura del proyecto:

```
mi-proyecto-docs/
├── public/
│   └── favicon.svg
├── src/
│   ├── assets/
│   │   └── houston.webp
│   ├── content/
│   │   └── docs/
│   │       ├── guides/
│   │       │   └── example.md
│   │       ├── index.mdx
│   │       └── reference/
│   │           └── example.md
│   └── env.d.ts
├── astro.config.mjs
├── package-lock.json
├── package.json
├── README.md
├── tailwind.config.mjs
└── tsconfig.json

```

*   **`public/`**: Almacena activos estáticos como favicon.
*   **`src/assets/`**: Contiene imágenes y otros activos utilizados en su documentación.
*   **`src/content/`**: Alberga sus archivos Markdown o MDX que componen el contenido de la documentación.
*   **`src/content/docs/`**: La ubicación predeterminada donde Starlight busca archivos Markdown o MDX.
*   **`astro.config.mjs`**: Configura los ajustes e integraciones de Starlight para todo el sitio.
*   **`package.json`**: Define los metadatos y las dependencias del proyecto.
*   **`tsconfig.json`**: Configuración para TypeScript (si se usa). 

## Ejecutar el Servidor de Desarrollo

1.  **Iniciar el servidor de desarrollo**:

```bash
npm run dev
```

Este comando inicia el servidor de desarrollo, generalmente en `http://localhost:4321/`. Abra su navegador web y navegue a esta dirección para ver su sitio de documentación de Starlight.

2.  **Editar contenido**: A medida que realice cambios en sus archivos Markdown o MDX dentro del directorio `src/content/docs/`, el servidor de desarrollo reconstruirá y actualizará automáticamente el sitio en su navegador, lo que le permitirá ver los cambios en tiempo real.

## Construir para Producción

1.  **Construir el sitio**: Cuando esté listo para implementar su sitio de documentación, ejecute el siguiente comando:

```bash
npm run build
```

Este comando genera una versión lista para producción de su sitio dentro del directorio `dist/`. 
