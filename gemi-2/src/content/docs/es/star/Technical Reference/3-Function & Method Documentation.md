---
title: Documentación de la función: generateText()
description: Una guía completa del método generateText() dentro de la clase OpenAIService.
---

## Método generateText()

El método `generateText()` es una funcionalidad central de la clase `OpenAIService`, responsable de enviar indicaciones a la API de OpenAI y recuperar respuestas de texto generadas. 

### Sintaxis

```javascript
generateText(prompt: string): Promise<OpenAIResponse>
```

### Parámetros

*   **prompt:** (string) La indicación de texto o consulta que se enviará a la API de OpenAI para generar texto. 

### Valor de retorno

*   **Promise\<OpenAIResponse\>**: Una promesa que se resuelve en un objeto `OpenAIResponse`. Este objeto encapsula la respuesta de la API, incluido el texto generado y otra información relevante.

### Ejemplo de uso 

```javascript
const openAIService = new OpenAIService('your-api-key');
const prompt = 'Escribe un poema sobre la belleza de la naturaleza.';

openAIService.generateText(prompt)
  .then(response => {
    console.log(response.text); // Acceder al poema generado
  })
  .catch(error => {
    console.error('Se ha producido un error:', error);
  });
```

### Gestión de errores

El método `generateText()` puede lanzar excepciones si se producen errores durante la solicitud de la API o el procesamiento de la respuesta. Es esencial implementar mecanismos adecuados de gestión de errores para gestionar estas situaciones con elegancia.

### Notas adicionales

*   El método `generateText()` utiliza la biblioteca `axios` para realizar solicitudes HTTP a la API de OpenAI. 
*   El tipo `OpenAIResponse` debe definirse con precisión en tu proyecto para representar la estructura de la respuesta de la API. 
*   Siempre respeta las pautas de uso y los límites de velocidad de OpenAI al interactuar con su API. 



