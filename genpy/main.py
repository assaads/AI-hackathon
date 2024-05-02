import os
from file_reader import read_files_from_directory
from gemini_client import init
from code_parser import generate_combined_file
from documentation_processor import handler

def main():     
    # Get the codebase directory from the user
    codebase_directory = input("Enter the path to the codebase directory: ")

    # Get the name of the project
    project_name = input("Enter the name of the project: ")

    init(generate_combined_file(codebase_directory))

    handler(project_name)

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