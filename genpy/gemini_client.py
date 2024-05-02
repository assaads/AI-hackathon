import base64
from google.cloud import aiplatform
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

vertexai.init(project="ornate-charter-422015", location="us-central1")
model = GenerativeModel(
"gemini-1.5-pro-preview-0409",
)
generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}
safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

chat = model.start_chat()

def generate_documentation(file_content: str) -> str:
    
    prompt= f"""Generate documentation for the following code:\n\n{file_content}\n
    do it in the format below:\n
    ---
    title: Example Guide
    description: A guide in my new Starlight docs site.
    ---

    * the format always starts with the title and description as above *

    use headings as shown below:
    # Heading1
    ## Heading2
    ### Heading3

    Guides lead a user through a specific task they want to accomplish, often with a sequence of steps.
    Writing a good guide requires thinking about what your users are trying to do. (this is a random text, text is used an normal)

    - bullet point is used as such as well
    Links are done this way: [name](link itself). for example: [about reference](https://diataxis.fr/reference/)
    """
    text_response = []
    responses = chat.send_message(prompt, stream=True,
      generation_config=generation_config,
      safety_settings=safety_settings)
    for chunk in responses:
        text_response.append(chunk.text)
    return "".join(text_response)

# def check_context():
#     prompt= """
#     summarize the code that I just sent you
#     """
#     text_response = []
#     responses = chat.send_message(prompt, stream=True,
#       generation_config=generation_config,
#       safety_settings=safety_settings)
#     for chunk in responses:
#         text_response.append(chunk.text)
#     return "".join(text_response)




# import vertexai

# from vertexai.generative_models import GenerativeModel, ChatSession

# # TODO(developer): Update and un-comment below lines
# project_id = "PROJECT_ID"
# location = "us-central1"
# vertexai.init(project=project_id, location=location)
# model = GenerativeModel(model_name="gemini-1.5-pro-preview-0409")
# chat = model.start_chat()

# def get_chat_response(chat: ChatSession, prompt: str) -> str:
#     text_response = []
#     responses = chat.send_message(prompt, stream=True)
#     for chunk in responses:
#         text_response.append(chunk.text)
#     return "".join(text_response)

# prompt = "Hello."
# print(get_chat_response(chat, prompt))

# prompt = "What are all the colors in a rainbow?"
# print(get_chat_response(chat, prompt))

# prompt = "Why does it appear when it rains?"
# print(get_chat_response(chat, prompt))

