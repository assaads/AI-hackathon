---
title: OpenAI API Reference 
description: Documentation for the OpenAI API as utilized within the Starlight documentation system.
---

# OpenAI API Reference 

## Overview

This reference documents the OpenAI API, specifically the `/v1/completions` endpoint, which is used for generating text completions with the `davinci-codex` engine. The `OpenAIService` class within the codebase interacts with this API to provide text generation capabilities. 

## Authentication

- **API Key:** All requests to the OpenAI API require authentication using your API key. This key should be kept confidential and securely stored.

## `/v1/completions` Endpoint

This endpoint is used to generate text completions based on a provided prompt. 

### Request Method

`POST`

### Request URL

`https://api.openai.com/v1/completions`

### Request Headers 

```
Content-Type: application/json
Authorization: Bearer YOUR_API_KEY 
```

### Request Body

```json
{
  "model": "davinci-codex", 
  "prompt": "YOUR_PROMPT_TEXT", 
  "temperature": 0,
  "max_tokens": 150,
  "top_p": 1,
  "frequency_penalty": 0.0, 
  "presence_penalty": 0.0,
  "stop": ["```"] 
}
``` 

#### Request Body Parameters

- **model (string):** The ID of the OpenAI model to use. In this case, `"davinci-codex"`.
- **prompt (string):** The text prompt to send to the API. This is the input text that the model will use to generate completions. 
- **temperature (number):** Controls the randomness of the generated text. Lower values (e.g., `0`) result in more deterministic and focused outputs, while higher values introduce more creativity and variety.
- **max_tokens (integer):** The maximum number of tokens (roughly corresponding to words) to generate in the completion. 
- **top_p (number):** Controls the diversity of the generated text by adjusting the probability distribution of the next token. 
- **frequency_penalty (number):** Penalizes tokens that appear frequently in the prompt, reducing repetition in the generated text. 
- **presence_penalty (number):** Penalizes tokens that are already present in the text, encouraging the model to generate novel content. 
- **stop (array of strings):** A list of strings that, if encountered, will cause the model to stop generating further text. 

### Response 

```json
{
  "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
  "object": "text_completion",
  "created": 1589478378,
  "model": "davinci-codex",
  "choices": [
    {
      "text": "\n```javascript\nfunction isEven(n) {\n  return n % 2 === 0;\n}\n```",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ]
}

```

#### Response Body Parameters 

- **id (string):** The ID of the completion. 
- **object (string):**  The type of object returned, in this case, `"text_completion"`.
- **created (integer):**  A Unix timestamp representing the time the completion was created.
- **model (string):** The ID of the model used to generate the completion. 
- **choices (array):**  An array of completion objects, each with the following properties: 
   - **text (string):** The generated text completion. 
   - **index (integer):** The index of the choice within the array. 
   - **logprobs (object):**  Information about the probability of each generated token.
   - **finish_reason (string):** The reason why the completion finished generating. 


## Example Request

```bash
curl https://api.openai.com/v1/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
  "model": "davinci-codex",
  "prompt": "Write a Python function that checks if a number is even:",
  "temperature": 0,
  "max_tokens": 150,
  "top_p": 1,
  "frequency_penalty": 0.0,
  "presence_penalty": 0.0,
  "stop": ["```"]
}'

```

## Example Response 

See the "Response" section above for an example JSON response. 



