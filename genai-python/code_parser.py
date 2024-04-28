from language_parser import LanguageParser
from python_parser import PythonParser
from file_utils import get_file_extension

class CodeParser:
    def __init__(self):
        self.language_parsers = {
            'py': PythonParser(),
            # Add other language parsers here as needed
        }
    
    def parse_file(self, file_path):
        extension = get_file_extension(file_path)
        parser = self.language_parsers.get(extension)
        if parser:
            parser.parse(file_path)
        else:
            print(f"No parser available for files with extension: {extension}")