---
title: Guías prácticas: Proyecto Starlight
description: Instrucciones detalladas para realizar tareas específicas dentro del proyecto Starlight.
---

## Cómo integrar la API de OpenAI

Esta guía proporciona un proceso paso a paso para integrar la API de OpenAI en tu proyecto Starlight para aprovechar sus capacidades de generación de lenguaje.

### Paso 1: Instalar el paquete requerido

Comienza instalando el paquete `openai`, que proporciona una interfaz conveniente para interactuar con la API de OpenAI:

```bash
npm install openai
```

o

```bash
yarn add openai
```

### Paso 2: Configurar las credenciales de la API de OpenAI

1.  **Obtener la clave API:** Si aún no lo has hecho, crea una cuenta en la plataforma OpenAI y adquiere tu clave API.
2.  **Almacenar la clave API de forma segura:** Es crucial almacenar tu clave API de forma segura. Considera usar variables de entorno o una solución de gestión de secretos para evitar exponerla en tu código.

### Paso 3: Crear un servicio OpenAI

1.  **Importar la biblioteca:** Importa las clases `Configuration` y `OpenAIApi` del paquete `openai`:

```javascript
import { Configuration, OpenAIApi } from 'openai';
```

2.  **Instanciar la configuración:** Crea una instancia de `Configuration` utilizando tu clave API:

```javascript
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY, // Reemplaza con tu variable de entorno de clave API
});
```

3.  **Instanciar OpenAIApi:** Crea una instancia de la clase `OpenAIApi`:

```javascript
const openai = new OpenAIApi(configuration);
```

### Paso 4: Utilizar los métodos de la API de OpenAI

La instancia `openai` ahora te otorga acceso a varios métodos de la API de OpenAI. Por ejemplo, para generar texto: 

```javascript
const response = await openai.createCompletion({
  model: 'text-davinci-003', // Especifica el modelo deseado
  prompt: 'Escribe un poema sobre el océano.', // Proporciona tu prompt
  max_tokens: 50, // Establece el número máximo de tokens a generar 
});

console.log(response.data.choices[0].text); // Accede al texto generado
```

Explora la [referencia de la API de OpenAI](https://beta.openai.com/docs/api-reference) para obtener una lista completa de los métodos y parámetros disponibles.

## Cómo implementar tu sitio Starlight

Esta guía describe los pasos para implementar tu proyecto Starlight en una plataforma de alojamiento en vivo, haciéndolo accesible al mundo.

### Paso 1: Elegir un proveedor de alojamiento

Selecciona un proveedor de alojamiento que se ajuste a tus requisitos y presupuesto. Algunas opciones populares incluyen:

*   **Netlify:** Ofrece una interfaz fácil de usar y una integración perfecta con repositorios Git.
*   **Vercel:** Proporciona un excelente rendimiento y escalabilidad.
*   **GitHub Pages:** Una opción conveniente para alojar sitios estáticos directamente desde tu repositorio de GitHub.

### Paso 2: Configurar los ajustes de implementación

1.  **Comando de compilación:** Especifica el comando para compilar tu proyecto Starlight para producción. Normalmente, esto implica ejecutar `npm run build` o `yarn build`.
2.  **Directorio de salida:** Indica el directorio donde se encuentran los archivos compilados después del proceso de compilación. Este suele ser el directorio `dist/`.

### Paso 3: Conectar a tu repositorio Git

Establece una conexión entre tu proveedor de alojamiento y tu repositorio Git que contiene el proyecto Starlight. Esto permite implementaciones automáticas cada vez que envías cambios a tu repositorio. 

### Paso 4: Implementar tu sitio

Inicia el proceso de implementación. Tu proveedor de alojamiento compilará tu proyecto y lo pondrá en línea en Internet.

### Paso 5: Configurar un dominio personalizado (opcional)

Si lo deseas, configura un nombre de dominio personalizado para que apunte a tu sitio Starlight implementado, proporcionando una presencia en línea más personalizada y profesional. 
