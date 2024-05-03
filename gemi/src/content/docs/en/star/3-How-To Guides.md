---
title: Starlight Project How-To Guides
description: Detailed instructions for accomplishing specific tasks within the Starlight project.
---

## How to Integrate OpenAI API

This guide provides a step-by-step process for integrating the OpenAI API into your Starlight project to leverage its language generation capabilities.

### Step 1: Install the Required Package

Begin by installing the `openai` package, which provides a convenient interface for interacting with the OpenAI API:

```bash
npm install openai
```

or

```bash
yarn add openai
```

### Step 2: Set Up OpenAI API Credentials

1.  **Obtain API Key:** If you haven't already, create an account on the OpenAI platform and acquire your API key.
2.  **Store API Key Securely:** It's crucial to store your API key securely. Consider using environment variables or a secrets management solution to avoid exposing it in your code. 

### Step 3: Create an OpenAI Service

1.  **Import the Library:** Import the `Configuration` and `OpenAIApi` classes from the `openai` package:

```javascript
import { Configuration, OpenAIApi } from 'openai';
```

2.  **Instantiate Configuration:** Create a `Configuration` instance using your API key:

```javascript
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY, // Replace with your API key environment variable
});
```

3.  **Instantiate OpenAIApi:** Create an instance of the `OpenAIApi` class:

```javascript
const openai = new OpenAIApi(configuration);
```

### Step 4: Utilize OpenAI API Methods

The `openai` instance now grants you access to various OpenAI API methods. For example, to generate text:

```javascript
const response = await openai.createCompletion({
  model: 'text-davinci-003', // Specify the desired model
  prompt: 'Write a poem about the ocean.', // Provide your prompt
  max_tokens: 50, // Set the maximum number of tokens to generate
});

console.log(response.data.choices[0].text); // Access the generated text
```

Explore the [OpenAI API reference](https://beta.openai.com/docs/api-reference) for a comprehensive list of available methods and parameters.

## How to Deploy Your Starlight Site

This guide outlines the steps to deploy your Starlight project to a live hosting platform, making it accessible to the world. 

### Step 1: Choose a Hosting Provider

Select a hosting provider that aligns with your requirements and budget. Popular options include:

*   **Netlify:** Offers a user-friendly interface and seamless integration with Git repositories.
*   **Vercel:** Provides excellent performance and scalability.
*   **GitHub Pages:** A convenient choice for hosting static sites directly from your GitHub repository. 

### Step 2: Configure Deployment Settings

1.  **Build Command:** Specify the command to build your Starlight project for production. Typically, this involves running `npm run build` or `yarn build`.
2.  **Output Directory:** Indicate the directory where the built files are located after the build process. This is usually the `dist/` directory. 

### Step 3: Connect to Your Git Repository

Establish a connection between your hosting provider and your Git repository containing the Starlight project. This enables automated deployments whenever you push changes to your repository.

### Step 4: Deploy Your Site

Initiate the deployment process. Your hosting provider will build your project and make it live on the internet.

### Step 5: Configure Custom Domain (Optional)

If desired, set up a custom domain name to point to your deployed Starlight site, providing a more personalized and professional online presence. 
