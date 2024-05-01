import os
from file_reader import read_files_from_directory
from openai_client import generate_documentation

def main():     
    codebase_directory = input("Enter the path to the codebase directory: ")
    files_contents = read_files_from_directory(codebase_directory)
    
    for file_path, content in files_contents.items():
        documentation = generate_documentation(content)
        doc_file_path = f"{file_path}.md"
        with open(doc_file_path, 'w', encoding='utf-8') as doc_file:
            doc_file.write(documentation)
        print(f"Documentation for {os.path.basename(file_path)} saved to {doc_file_path}")

if __name__ == "__main__":
    main()