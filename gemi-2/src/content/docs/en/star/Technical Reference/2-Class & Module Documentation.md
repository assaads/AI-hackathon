---
title: Class Documentation: OpenAIService
description: A detailed overview of the OpenAIService class and its functionalities.
---

## OpenAIService Class

The `OpenAIService` class serves as a dedicated interface for interacting with the OpenAI API, specifically for generating text completions using the `davinci-codex` engine.

### Constructor

```javascript
constructor(apiKey: string)
```

*   **apiKey:** (string) Your OpenAI API key, essential for authentication and access to the API.

### Methods

*   **generateText(prompt: string): Promise\<OpenAIResponse\>**
    *   **prompt:** (string) The input prompt or query that will be sent to the OpenAI API to generate text.
    *   **Returns:** (Promise\<OpenAIResponse\>) A Promise that resolves to an `OpenAIResponse` object containing the API's response, including the generated text. 

**Example Usage:**

```javascript
const openAIService = new OpenAIService('your-api-key');
const prompt = 'Explain the concept of artificial intelligence.';

openAIService.generateText(prompt)
  .then(response => {
    console.log(response.text); // Access the generated text
  })
  .catch(error => {
    console.error('An error occurred:', error);
  });
```

### Properties

*   **apiKey:** (string) Stores the OpenAI API key used for authentication. 

## Additional Notes

*   The `OpenAIService` class relies on the `axios` library for making HTTP requests to the OpenAI API.
*   Ensure that the `OpenAIResponse` type is defined appropriately in your project (refer to the `types` file).
*   Always adhere to OpenAI's usage guidelines and rate limits when utilizing their services. 
