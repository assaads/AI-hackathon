import os

class FileScanner:
    def __init__(self, root_directory):
        self.root_directory = root_directory
    
    def scan(self):
        """Walk through the directories starting from root_directory and list all code files."""
        code_files = []
        for root, dirs, files in os.walk(self.root_directory):
            for file in files:
                if file.endswith(".py"):  # Assuming we're only interested in Python files
                    code_files.append(os.path.join(root, file))
        return code_files