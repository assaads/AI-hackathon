---
title: Environment Variables
description: A guide to utilizing environment variables within the Starlight project.
---

## Environment Variables

Environment variables offer a way to configure your Starlight project with external values without hardcoding them directly into your code. This is particularly useful for managing sensitive information like API keys or database credentials.

### OPENAI\_API\_KEY

*   **Purpose:** Stores the API key for accessing the OpenAI API. 
*   **Required:** Yes, if you intend to use the OpenAI integration for text generation.
*   **How to Set:**
    1.  Create a `.env` file in the root directory of your project.
    2.  Add the following line to the `.env` file, replacing `your-api-key` with your actual OpenAI API key:

```
OPENAI_API_KEY=your-api-key
```

*   **Default Value:** None

### Other Environment Variables

The Starlight project can be further customized using additional environment variables depending on your specific requirements and integrations. 

## Setting Environment Variables

*   **.env file:** Create a `.env` file in your project's root directory to store environment variables. Each line in the file should follow the format `VARIABLE_NAME=value`.
*   **Terminal:** Set environment variables directly in your terminal session using the export command:

```bash
export OPENAI_API_KEY=your-api-key
```

*   **Hosting Platforms:** Many hosting platforms provide mechanisms for setting environment variables through their dashboards or configuration files. 

## Important Considerations

*   **Security:** Avoid committing your `.env` file to version control, especially if it contains sensitive information.
*   **Variable Scope:** Environment variables set in the terminal are only available within that specific session.
*   **Best Practices:** Follow secure coding practices and avoid exposing API keys or secrets in client-side code. 



