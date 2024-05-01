from google.cloud import gemini

def generate_documentation(myprompt):
    # Create a client
    client = gemini.GeminiClient()

    # Create a request
    request = gemini.DocumentRequest(
        parent="projects/your-project-id/locations/us-central1/models/default",
        document_input=gemini.DocumentInput(text=myprompt)
    )

    # Call the Gemini API
    response = client.document(request=request)

    # Return the generated text
    return response.document.text
