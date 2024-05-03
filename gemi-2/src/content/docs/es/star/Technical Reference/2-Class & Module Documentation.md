---
title: Documentación de la clase: OpenAIService
description: Una descripción detallada de la clase OpenAIService y sus funcionalidades.
---

## Clase OpenAIService

La clase `OpenAIService` sirve como una interfaz dedicada para interactuar con la API de OpenAI, específicamente para generar completaciones de texto utilizando el motor `davinci-codex`.

### Constructor

```javascript
constructor(apiKey: string)
```

*   **apiKey:** (string) Tu clave API de OpenAI, esencial para la autenticación y el acceso a la API. 

### Métodos

*   **generateText(prompt: string): Promise\<OpenAIResponse\>**
    *   **prompt:** (string) El prompt o consulta de entrada que se enviará a la API de OpenAI para generar texto. 
    *   **Returns:** (Promise\<OpenAIResponse\>) Una promesa que se resuelve en un objeto `OpenAIResponse` que contiene la respuesta de la API, incluido el texto generado.

**Ejemplo de uso:**

```javascript
const openAIService = new OpenAIService('your-api-key');
const prompt = 'Explica el concepto de inteligencia artificial.';

openAIService.generateText(prompt)
  .then(response => {
    console.log(response.text); // Acceder al texto generado
  })
  .catch(error => {
    console.error('Se ha producido un error:', error);
  });
```

### Propiedades

*   **apiKey:** (string) Almacena la clave API de OpenAI utilizada para la autenticación.

## Notas adicionales

*   La clase `OpenAIService` se basa en la biblioteca `axios` para realizar solicitudes HTTP a la API de OpenAI.
*   Asegúrate de que el tipo `OpenAIResponse` esté definido correctamente en tu proyecto (consulta el archivo `types`).
*   Siempre respeta las pautas de uso y los límites de velocidad de OpenAI al utilizar sus servicios. 


