from openai import OpenAI
from config import OPENAI_API_KEY


def generate_documentation(file_content):
    """
    Sends file content to the OpenAI API and returns the generated documentation.
    """
    client = OpenAI(api_key=OPENAI_API_KEY)

    myprompt= f"""Generate documentation for the following code:\n\n{file_content}\n
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

    - bullet point is used as such as well"""

    # response = client.completions.create(model="gpt-4-1106-preview",
    # prompt=myprompt,
    # temperature=0.5,
    # max_tokens=8024,
    # top_p=1.0,
    # frequency_penalty=0.0,
    # presence_penalty=0.0)

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "user", "content": myprompt}
        ]
    )

    return response.choices[0].message.content