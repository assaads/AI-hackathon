import os
from gemini_client import init
from code_parser import generate_combined_file
from documentation_processor import handler
from language_processor import choose_languages

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
















# # Define the output directory
# output_directory = "./gemi/src/content/docs/project/"

# # Read files and generate documentation
# files_contents = read_files_from_directory(codebase_directory)

# for file_path, content in files_contents.items():
#     documentation = generate_documentation(content)
#     relative_path = os.path.relpath(file_path, codebase_directory)
#     relative_path_without_extension = os.path.splitext(relative_path)[0]
#     doc_file_path = os.path.join(output_directory, f"{relative_path_without_extension}.md")
    
#     # Ensure directories exist for the output file
#     os.makedirs(os.path.dirname(doc_file_path), exist_ok=True)
    
#     # Write the documentation into the output file
#     with open(doc_file_path, 'w', encoding='utf-8') as doc_file:
#         doc_file.write(documentation)
    
#     print(f"Documentation for {os.path.basename(file_path)} saved to {doc_file_path}")

# print(check_context())