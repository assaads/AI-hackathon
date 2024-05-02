---
title: OpenAIService Usage Guide
description: A guide for utilizing the OpenAIService class to interact with the OpenAI API.
---

# Introduction
This guide provides instructions on how to use the `OpenAIService` class to generate text completions using the OpenAI API, specifically the davinci-codex engine. The class is designed to facilitate the communication with the API by sending prompts and receiving the generated responses.

## Prerequisites
- Node.js environment
- An API key from OpenAI
- `axios` library installed
- `OpenAIResponse` type defined in the `types` file

## Quick Start
To begin using the `OpenAIService`, follow these steps:

1. Obtain the API key by creating an account on the OpenAI platform.
2. Install the `axios` library using the `npm` package manager.
3. Import the `OpenAIService` class and the `OpenAIResponse` type from their respective files in your project.

## Initialization
Create an instance of the `OpenAIService` class by passing your API key as a parameter to the constructor.

```javascript
import { OpenAIService } from 'path-to-OpenAIService-file';

const apiKey = 'your-api-key-here'; // Replace with your actual API key
const openAIService = new OpenAIService(apiKey);
```

## Generating Documentation with the OpenAI API
Use the `generateDocumentation` method to send a prompt to the OpenAI API and receive a response.

### Using the Generate Documentation Method
- The method takes a `prompt` string as input and returns a `Promise` that resolves to an `OpenAIResponse` object.

Example:
```javascript
const prompt = 'Translate the following Python code to JavaScript:';
openAIService.generateDocumentation(prompt)
  .then(response => {
    console.log(response);
  })
  .catch(error => {
    console.error('An error occurred:', error);
  });
```

### Response Handling
Upon a successful API call, the method returns a response object which includes properties such as the generated text. In the case of an error, it logs the error and rethrows it for further handling.

## Conclusion
The `OpenAIService` class provides a seamless interface for interacting with the OpenAI API. By following this guide, you should be able to integrate OpenAI's powerful language generation capabilities into your applications.

Remember to adhere to OpenAI's usage guidelines and rate limits when utilizing their services.

# Additional Resources
- OpenAI Documentation: https://beta.openai.com/docs/
- Axios Documentation: https://axios-http.com/docs/intro
- Node.js Documentation: https://nodejs.org/en/docs/