import base64
from google.cloud import aiplatform
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

vertexai.init(project="my-second-project-422200", location="us-central1")
model = GenerativeModel(
"gemini-1.5-pro-preview-0409",
)
generation_config = {
    "max_output_tokens": 8192,
    "temperature": 0.8,
    "top_p": 0.95,
}
safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

chat = model.start_chat()

def init(codebase):
    print("Initializing gemini agent")
    define_format()
    send_codebase(codebase)

def define_format():
    prompt= """
    I would like you to act as a professional/expert developer and technical architect.
    I am about to send you the full codebase of a project. After I do I will start giving you requests regarding the code, mainly aimed at creating documentation for the codebase.
    Everytime I request something from you I would like you to give me the answer in the format below (even if I asked you about a documentation regarding the code that you don't find or deem not applicable in the specific source code I would still like you to give me you answer in the following format without anything else before or after in the chat): 
    ---
    title: Example Guide
    description: A guide in my new Starlight docs site.
    ---

    don't include anything before this:
    "
    ---
    title: Example Guide
    description: A guide in my new Starlight docs site.
    ---
    " 
    as the page always starts with it. Also, don't add a heading1 title after this section again but start directly with the content after.

    Moreover if requested to create a page in a different language, only what comes after "title:" and "description:" is in a different language for the start of the page.
    for example:
    for french:
    "
    ---
    title: Bonjour 
    description: comment ca va
    ---
    " 

    use headings as shown below:
    # Heading1
    ## Heading2
    ### Heading3
    #### Heading4


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
    print("Finished defining UI format to AI")
    return "".join(text_response)

def send_codebase(codebase: str):
    prompt= f"""
    Here is the entire codebase of the project. I have put the name of the folder and files about each of their content for clarity.
    Keep in mind that I will be asking you documentation generation request following it.
    here is the entire codebase:
    {codebase}
    """
    text_response = []
    responses = chat.send_message(prompt, stream=True,
      generation_config=generation_config,
      safety_settings=safety_settings)
    for chunk in responses:
        text_response.append(chunk.text)
    print("Finished sending the codebase to the AI")
    return "".join(text_response)

def request_documentation(documentation_subject: str, language: str):
    add_language=""
    if language!="":
        add_language= f" in the {language} language"
    
    prompt= f"""
    In the format requested previouly (even if I asked you to generate a documentation that you don't find or deem not applicable in the specific source code I would still like you to give me you answer in the format requested previouly, and don't add any text before or after that's not in the format in your answer) and based on the codebase sent, please create a documentation document for the following section and it's description{add_language}:
    {documentation_subject}
    """
    text_response = []
    responses = chat.send_message(prompt, stream=True,
      generation_config=generation_config,
      safety_settings=safety_settings)
    for chunk in responses:
        text_response.append(chunk.text)
    # print(f"Finished generating documentation for {documentation_subject}")
    return "".join(text_response)






















# def generate_documentation(file_content: str) -> str:
    
#     prompt= f"""Generate documentation for the following code:\n\n{file_content}\n
#     do it in the format below:\n
#     ---
#     title: Example Guide
#     description: A guide in my new Starlight docs site.
#     ---

#     * the format always starts with the title and description as above *

#     use headings as shown below:
#     # Heading1
#     ## Heading2
#     ### Heading3
#     #### Heading4

#     Guides lead a user through a specific task they want to accomplish, often with a sequence of steps.
#     Writing a good guide requires thinking about what your users are trying to do. (this is a random text, text is used an normal)

#     - bullet point is used as such as well
#     Links are done this way: [name](link itself). for example: [about reference](https://diataxis.fr/reference/)
#     """
#     text_response = []
#     responses = chat.send_message(prompt, stream=True,
#       generation_config=generation_config,
#       safety_settings=safety_settings)
#     for chunk in responses:
#         text_response.append(chunk.text)
#     return "".join(text_response)


















# def func():
#     prompt= f"""
    
#     """
#     text_response = []
#     responses = chat.send_message(prompt, stream=True,
#       generation_config=generation_config,
#       safety_settings=safety_settings)
#     for chunk in responses:
#         text_response.append(chunk.text)
#     return "".join(text_response)


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

