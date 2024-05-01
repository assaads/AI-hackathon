import os

def read_files_from_directory(directory_path):
    """
    Reads all files in the specified directory and returns their paths and contents.
    """
    files_contents = {}
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as file_content:
                files_contents[file_path] = file_content.read()
    return files_contents