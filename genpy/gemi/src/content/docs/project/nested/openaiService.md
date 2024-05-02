---
title: OpenAIService Class Guide
description: Understanding and utilizing the OpenAIService class for interacting with the OpenAI API.
---

# OpenAIService Class: Interacting with OpenAI API

This guide explores the `OpenAIService` class, its purpose, and how to use it for generating text through the OpenAI API.

## Overview

The `OpenAIService` class provides a convenient way to interact with the OpenAI API, specifically for generating text completions using the "davinci-codex" engine. 

## Initialization

To use the `OpenAIService` class, you first need to create an instance by providing your OpenAI API key:

```javascript
import { OpenAIService } from './path/to/OpenAIService';

const apiKey = 'YOUR_API_KEY';
const openai = new OpenAIService(apiKey);
```

## Generating Text

The primary function of this class is `generateDocumentation(prompt)`. This asynchronous function sends a request to the OpenAI API with the provided `prompt` string and returns a Promise containing the API response.

### Parameters

* **prompt (string):** The text prompt that serves as the starting point for generating text completions.

### Response

The function returns a Promise that resolves to an `OpenAIResponse` object, containing the generated text and other relevant information from the API. Refer to the `OpenAIResponse` type definition for details on its structure. 

### Example Usage

```javascript
const prompt = "Write a short story about a robot exploring a new planet.";

openai.generateDocumentation(prompt)
  .then(response => {
    console.log(response.choices[0].text);
  })
  .catch(error => {
    console.error("Error generating text:", error);
  });
```

## Additional Notes

* The class assumes you have the `axios` library installed for making HTTP requests.
* Error handling is included to log errors and re-throw them for further handling in your application.
* The API request parameters, such as `temperature` and `max_tokens`, are set with default values suitable for many use cases but can be customized if needed. 

## Further Exploration

* Explore the OpenAI API documentation: [OpenAI API Reference](https://beta.openai.com/docs/api-reference)
* Learn more about the available engines and their capabilities.
* Experiment with different parameter settings to fine-tune the generated text output. 
