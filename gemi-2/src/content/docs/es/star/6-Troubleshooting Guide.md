---
title: Guía de solución de problemas
description: Soluciones a problemas comunes que se encuentran al trabajar con el proyecto Starlight.
---

## Problemas comunes

### El servidor de desarrollo no se inicia

*   **Problema:** Cuando ejecutas `npm run dev` o `yarn dev`, el servidor de desarrollo no se inicia o arroja errores.
*   **Posibles causas:**
    *   Conflicto de puertos: Es posible que otra aplicación esté utilizando el mismo puerto (el predeterminado es 3000). 
    *   Dependencias faltantes: Es posible que las dependencias requeridas no estén instaladas correctamente.
    *   Errores de configuración: Puede haber errores en tu archivo `astro.config.mjs`.
*   **Soluciones:**
    *   Cambiar el puerto: Modifica el número de puerto en el archivo `astro.config.mjs` o utiliza la marca `--port` al iniciar el servidor.
    *   Reinstalar dependencias: Ejecuta `npm install` o `yarn install` para asegurarte de que todas las dependencias estén instaladas. 
    *   Verificar la configuración: Revisa tu archivo `astro.config.mjs` para detectar cualquier error de sintaxis o configuración incorrecta.

### Los cambios de contenido no se reflejan

*   **Problema:** Después de realizar cambios en tus archivos de contenido Markdown o MDX, las actualizaciones no se reflejan en el sitio de desarrollo.
*   **Posibles causas:**
    *   Problemas de caché: El navegador o el servidor de desarrollo pueden estar almacenando en caché contenido antiguo.
    *   Rutas de archivo incorrectas: Es posible que estés editando los archivos incorrectos o que tengas rutas de archivo incorrectas en tu configuración.
*   **Soluciones:**
    *   Borrar caché: Borra la caché de tu navegador o reinicia el servidor de desarrollo para forzar una recarga. 
    *   Verificar las rutas de los archivos: Asegúrate de que estás editando los archivos de contenido correctos y de que las rutas de los archivos en tu archivo `astro.config.mjs` sean precisas.

### Problemas de estilo

*   **Problema:** Tu sitio Starlight no muestra los estilos correctamente o las clases de Tailwind CSS no se están aplicando. 
*   **Posibles causas:**
    *   Configuración de Tailwind CSS: Puede haber errores en tu archivo `tailwind.config.mjs`.
    *   Directivas de Tailwind faltantes: Es posible que hayas olvidado incluir las directivas de Tailwind necesarias en tus componentes de diseño o página.
*   **Soluciones:**
    *   Verificar la configuración de Tailwind: Revisa tu archivo `tailwind.config.mjs` y asegúrate de que las rutas de contenido y otras configuraciones sean correctas.
    *   Agregar directivas de Tailwind: Asegúrate de haber agregado las directivas `@tailwind` para base, componentes y utilidades en tus componentes de diseño o página donde deseas utilizar las clases de Tailwind. 

### Errores de la API de OpenAI

*   **Problema:** Encuentras errores al utilizar la integración de la API de OpenAI. 
*   **Posibles causas:** Consulta la sección dedicada a "Códigos y mensajes de error" para obtener explicaciones detalladas y soluciones para errores comunes de la API de OpenAI.

## Consejos adicionales

*   **Consultar la documentación:** Consulta la [documentación oficial de Starlight](https://starlight.astro.build/) y la [documentación de Astro](https://docs.astro.build/) para obtener información detallada y orientación para la solución de problemas.
*   **Soporte de la comunidad:** Busca ayuda en las comunidades de Starlight y Astro, donde puedes encontrar respuestas a preguntas comunes y obtener ayuda de usuarios experimentados. 
*   **Herramientas de depuración:** Utiliza las herramientas de desarrollo del navegador y las técnicas de depuración para identificar y resolver problemas de manera efectiva. 




