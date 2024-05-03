---
title: Error Codes and Messages: OpenAI API Integration
description: Troubleshooting common errors encountered when using the OpenAI API within the Starlight project. 
---

## OpenAI API Errors

While interacting with the OpenAI API, you might encounter various error codes and messages. Here are some common ones and guidance on how to address them:

*   **401 Unauthorized:**
    *   **Meaning:** This error indicates that your API key is invalid or missing.
    *   **Solution:**
        *   Verify that you have a valid API key from OpenAI.
        *   Ensure that you have correctly set the `OPENAI_API_KEY` environment variable.
        *   Check that you are using the correct API endpoint and request method.

*   **429 Too Many Requests:**
    *   **Meaning:** You have exceeded the rate limit for API requests.
    *   **Solution:**
        *   Reduce the frequency of your API calls.
        *   Consider upgrading your OpenAI plan for higher rate limits.

*   **400 Bad Request:**
    *   **Meaning:** The request you sent to the API is malformed or contains invalid parameters.
    *   **Solution:**
        *   Carefully review the API documentation and ensure that your request parameters are correct.
        *   Check for typos or missing required fields. 

*   **500 Internal Server Error:**
    *   **Meaning:** An error occurred on the OpenAI server side.
    *   **Solution:**
        *   Retry your request later.
        *   If the issue persists, contact OpenAI support. 

## General Troubleshooting Tips

*   **Check API Documentation:** Refer to the official [OpenAI API documentation](https://beta.openai.com/docs/api-reference) for detailed information about error codes, parameters, and response formats.
*   **Log API Responses:** Log the complete API response to gain insights into the specific error details.
*   **Validate Input:** Ensure that the input prompt or query you are sending to the API is valid and does not contain any errors or unsupported characters. 
*   **Test API Key:** Use the OpenAI Playground to test your API key and verify that it is functioning correctly. 
