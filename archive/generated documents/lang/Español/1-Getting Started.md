---
title: Primeros pasos
description: Una guía para que los nuevos usuarios instalen, configuren y comiencen a usar el proyecto rápidamente.
---

# Introducción
¡Bienvenido al proyecto! Esta guía te acompañará a través de los pasos para instalarlo, configurarlo y comenzar a usarlo.

## Prerrequisitos
Antes de empezar, asegúrate de tener lo siguiente:

* **Node.js y npm:** Verifica que tienes instalada la última versión de Node.js (https://nodejs.org) y npm (https://www.npmjs.com). 
* **Editor de código:** Elige un editor de código o IDE de tu preferencia, como Visual Studio Code (https://code.visualstudio.com).

## Instalación
1. **Clonar el proyecto:** Clona el repositorio del proyecto en tu computadora local. 
2. **Instalar dependencias:** En la terminal, navega hasta el directorio del proyecto y ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
npm install
```

## Configuración
1. **Configurar variables de entorno:** Crea un archivo `.env` en la raíz del proyecto y agrega las variables de entorno necesarias de acuerdo con los requisitos del proyecto.
2. **Configurar Starlight (opcional):** Si estás utilizando Starlight para la documentación, personaliza la configuración en el archivo `astro.config.mjs`.

## Ejecutar la aplicación
1. **Iniciar el servidor de desarrollo:** Ejecuta el siguiente comando para iniciar el servidor de desarrollo:

```bash
npm run dev
```

Esto iniciará el proyecto y lo hará accesible en `http://localhost:3000`.

2. **Construir el proyecto:** Para crear una versión de producción del proyecto, usa el siguiente comando:

```bash
npm run build
```

Esto construirá el proyecto en la carpeta `dist/`, lista para su implementación.

## Uso básico
Una vez que el proyecto esté en funcionamiento, puedes comenzar a usar las funciones del proyecto. Consulta la documentación del proyecto para obtener información más detallada sobre el uso específico. 
