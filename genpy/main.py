import os
from gemini_client import init
from code_parser import generate_combined_file
from documentation_processor import handler
from language_processor import choose_languages
from fe_builder import copy_directory

def main():     
    # Get the codebase directory from the user
    codebase_directory = input("Enter the path to the codebase directory (relative to the path of this program): ")

    # Get the name of the project
    project_name = input("Enter the name of the project: ")

    user_choice = input("Do you want to choose multiple languages (the default language is English)? (yes/no): ").lower()
    if user_choice == 'yes' or user_choice == 'y':
        languages_chosen=choose_languages()
        init(generate_combined_file(codebase_directory))
        # Process each selected language
        for lang in languages_chosen:
            handler(project_name, lang)
        print(f"Full Documentation generation done")
        return
    elif user_choice != 'no' or user_choice == 'n':
        raise ValueError("Invalid option. Please enter 'yes'/'y' or 'no'/'n'.")

    # Get style of writing for documentation
    # writing_style = input("Choose the writing complexity for your documentation: \n1-Comprehensible by a high shcool student\n2-Comprehensible by a graduate developer\n3-Comprehensible by an expert developer\n4-Gemini's default writing complexity(recommended)")

    init(generate_combined_file(codebase_directory))

    handler(project_name, "")

    print(f"Full Documentation generation done")

if __name__ == "__main__":
    main()