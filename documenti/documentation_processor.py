import os
import json
from gemini_client import request_documentation
import time

def handler(project_name: str, language=""):
    # Read the documentation sections and structure that we want from the following folder
    # Modify this folder (documentation_sections.json) in order to create you own structure and section name/description
    with open('documentation_sections.json', 'r') as f:
        input_dict = json.load(f)

    # Define the output directory
    dir = "../gemi/src/content/docs/"

    if language=="":
        # creating project directory within the UI repo
        new_dir = os.path.join(dir, project_name)
        os.makedirs(new_dir, exist_ok=True)
        output_dir = f"../gemi/src/content/docs/{project_name}"
    else:
        # creating project directory within the UI repo
        language_labels = {
        "English": "en",
        "Deutsch": "de",
        "Español": "es",
        "日本語": "ja",
        "Français": "fr",
        "Italiano": "it",
        "Bahasa Indonesia": "id",
        "简体中文": "zh-cn",
        "Português do Brasil": "pt-br",
        "Português": "pt",
        "한국어": "ko",
        "Türkçe": "tr",
        'Русский': 'ru',
        'हिंदी': 'hi',
        'Dansk': 'da',
        'Українська': 'uk'
        }
        language=language_labels.get(language)
        new_dir = os.path.join(dir, language, project_name)
        os.makedirs(new_dir, exist_ok=True)
        output_dir = f"../gemi/src/content/docs/{language}/{project_name}"

    process_dict(input_dict, process_item, output_dir, language)

def process_item(key, value, language):
    # This is where you can add your own logic to process each key-value pair
    print (f"processing {key}")
    section_topic=f"{key}: {value}"
    return request_documentation(section_topic, language)

def process_dict(input_dict, process_func, output_dir, language):
    prefix = 1
    for key, value in input_dict.items():
        if isinstance(value, dict):
            # If the value is a nested dictionary, create a new directory and process the nested dictionary
            new_dir = os.path.join(output_dir, f"{key}")
            os.makedirs(new_dir, exist_ok=True)
            process_dict(value, process_func, new_dir, language)
        else:
            # If the value is not a dictionary, process the key-value pair and write the result into a .md file
            result = process_func(key, value, language)
            with open(os.path.join(output_dir, f"{prefix}-{key}.md"), 'w', encoding='utf-8') as f:
                f.write(result)
            prefix += 1
