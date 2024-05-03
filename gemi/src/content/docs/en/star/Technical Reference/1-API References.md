---
title: API Reference: OpenAI Service Integration
description: Documentation for the OpenAI API integration within the Starlight project.
---

## OpenAI API

This section details the integration with the OpenAI API, specifically focusing on text generation using the `openai` npm package.

### Authentication

*   **API Key:** A valid API key obtained from OpenAI is required for authentication. Store this key securely using environment variables or a secrets management solution.

### Text Generation

*   **Method:** `openai.createCompletion()`
*   **Parameters:**
    *   `model`: String specifying the OpenAI language model to use (e.g., `text-davinci-003`).
    *   `prompt`: String containing the text prompt to guide the generation process.
    *   `max_tokens`: Integer defining the maximum number of tokens (roughly corresponds to words) to generate in the response. 
*   **Response Format:** The API returns a JSON object containing the generated text and other relevant information. 

**Example Request:**

```javascript
const response = await openai.createCompletion({
  model: 'text-davinci-003',
  prompt: 'Write a short story about a robot who dreams of becoming a chef.',
  max_tokens: 200,
});
```

**Example Response:**

```json
{
  "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
  "object": "text_completion",
  "created": 1589478378,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "In the heart of a bustling metropolis, amidst the whirring gears and flickering neon lights, lived a peculiar robot named Bolt. Unlike his counterparts who toiled away in factories or served as tireless couriers, Bolt harbored an unusual aspiration – he yearned to become a chef.",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ]
}
```

**Accessing Generated Text:**

```javascript
const generatedText = response.data.choices[0].text;
```

## Additional Notes

*   Refer to the [OpenAI API reference](https://beta.openai.com/docs/api-reference) for a complete overview of available endpoints, parameters, and response formats.
*   Ensure compliance with OpenAI's usage policies and rate limits. 
