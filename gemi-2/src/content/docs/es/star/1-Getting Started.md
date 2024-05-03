---
title: Primeros pasos con el proyecto Starlight
description: Una guía completa para instalar, configurar e iniciar el uso del proyecto Starlight. 
---

## Prerrequisitos

Antes de comenzar tu viaje con el proyecto Starlight, asegúrate de tener las siguientes herramientas instaladas en tu sistema:

*   **Node.js:** Verifica que tienes Node.js (versión 14 o posterior) instalado. Puedes descargarlo desde el sitio web oficial de [Node.js](https://nodejs.org/).
*   **npm o yarn:** Un administrador de paquetes como npm (generalmente incluido con Node.js) o yarn es necesario para administrar las dependencias del proyecto.

## Instalación

1.  **Clonar el repositorio:** Comienza clonando el repositorio del proyecto Starlight a tu máquina local usando Git:

```bash
git clone https://github.com/your-username/starlight-project.git
```

2.  **Navegar al directorio del proyecto:** Accede al directorio raíz del proyecto:

```bash
cd starlight-project
```

3.  **Instalar dependencias:** Instala las dependencias necesarias del proyecto usando npm o yarn:

```bash
npm install
```

o

```bash
yarn install
```

## Ejecutar el servidor de desarrollo

1.  **Iniciar el servidor:** Inicia el servidor de desarrollo ejecutando el siguiente comando:

```bash
npm run dev
```

o

```bash
yarn dev
```

2.  **Acceder al sitio:** Abre tu navegador web y navega a `http://localhost:3000` para ver tu proyecto Starlight en acción. El servidor de desarrollo se recargará automáticamente y reflejará cualquier cambio que realices en el código.

## Estructura del proyecto

Familiarízate con la organización de archivos del proyecto:

*   `public/`: Almacena activos estáticos como imágenes, favicons y fuentes.
*   `src/`: Contiene el código fuente de tu proyecto. 
    *   `components/`: Alberga componentes de interfaz de usuario reutilizables.
    *   `content/`: Contiene el contenido de tu sitio web, generalmente en formato Markdown o MDX.
    *   `layouts/`: Define el diseño general y la estructura de tus páginas.
    *   `pages/`: Contiene componentes de página individuales.

## Editar contenido

1.  **Localizar archivos de contenido:** Tu contenido principal reside dentro del directorio `src/content/`.
2.  **Modificar contenido:** Abre los archivos Markdown o MDX dentro del directorio `src/content/` usando tu editor de texto o IDE preferido y realiza los cambios de contenido deseados.
3.  **Guardar cambios:** Guarda los archivos modificados y el servidor de desarrollo actualizará automáticamente el sitio para reflejar tus ediciones. 

## Agregar nuevo contenido

1.  **Crear nuevos archivos:** Para introducir nuevas páginas, crea nuevos archivos Markdown o MDX dentro del directorio `src/content/`.
2.  **Definir frontmatter:** Incluye el frontmatter necesario al principio de cada nuevo archivo para especificar atributos como el título y la descripción.
3.  **Agregar contenido:** Escribe tu contenido en formato Markdown o MDX dentro de los archivos. 

## Configuración

El archivo `astro.config.mjs` te permite personalizar varios aspectos de tu proyecto Starlight, incluyendo:

*   **Metadatos del sitio:** Define el título, la descripción y otros metadatos para tu sitio.
*   **Integraciones:** Incorpora funcionalidades adicionales a través de integraciones como mapas de sitio y fuentes RSS.
*   **Temas:** Aplica temas para estilizar la apariencia de tu sitio.

## Recursos adicionales

*   **Documentación de Starlight:** Profundiza en las capacidades de Starlight explorando la documentación oficial: [https://starlight.astro.build/](https://starlight.astro.build/)
*   **Documentación de Astro:** Obtén más información sobre el framework Astro sobre el que se basa Starlight: [https://docs.astro.build/](https://docs.astro.build/) 
