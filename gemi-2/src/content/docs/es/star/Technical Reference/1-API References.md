---
title: Referencia de la API: Integración del servicio OpenAI
description: Documentación para la integración de la API de OpenAI dentro del proyecto Starlight.
---

## API de OpenAI

Esta sección detalla la integración con la API de OpenAI, centrándose específicamente en la generación de texto utilizando el paquete npm `openai`.

### Autenticación

*   **Clave API:** Se requiere una clave API válida obtenida de OpenAI para la autenticación. Almacena esta clave de forma segura utilizando variables de entorno o una solución de gestión de secretos. 

### Generación de texto

*   **Método:** `openai.createCompletion()`
*   **Parámetros:**
    *   `model`: Cadena que especifica el modelo de lenguaje OpenAI que se utilizará (por ejemplo, `text-davinci-003`).
    *   `prompt`: Cadena que contiene el prompt de texto para guiar el proceso de generación. 
    *   `max_tokens`: Entero que define el número máximo de tokens (aproximadamente corresponde a palabras) que se generarán en la respuesta.
*   **Formato de respuesta:** La API devuelve un objeto JSON que contiene el texto generado y otra información relevante.

**Ejemplo de solicitud:**

```javascript
const response = await openai.createCompletion({
  model: 'text-davinci-003',
  prompt: 'Escribe una historia corta sobre un robot que sueña con convertirse en chef.',
  max_tokens: 200,
});
```

**Ejemplo de respuesta:**

```json
{
  "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
  "object": "text_completion",
  "created": 1589478378,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "En el corazón de una bulliciosa metrópolis, en medio de los engranajes zumbantes y las luces de neón parpadeantes, vivía un robot peculiar llamado Bolt. A diferencia de sus homólogos que trabajaban duro en las fábricas o servían como mensajeros incansables, Bolt albergaba una aspiración inusual: anhelaba convertirse en chef.",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ]
}
```

**Acceder al texto generado:**

```javascript
const generatedText = response.data.choices[0].text;
```

## Notas adicionales

*   Consulta la [referencia de la API de OpenAI](https://beta.openai.com/docs/api-reference) para obtener una descripción general completa de los endpoints, parámetros y formatos de respuesta disponibles.
*   Asegúrate de cumplir con las políticas de uso y los límites de velocidad de OpenAI. 
