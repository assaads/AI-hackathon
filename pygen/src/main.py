from file_scanner import FileScanner
from code_parser import CodeParser
from data_organizer import DataOrganizer

def main():
    # Define the root directory of the codebase to parse
    root_directory = "./path/to/codebase"
    
    # Initialize components
    scanner = FileScanner(root_directory)
    parser = CodeParser()
    organizer = DataOrganizer()
    
    # Scan for files
    files = scanner.scan()
    
    # Parse files and organize data
    for file_path in files:
        code_data = parser.parse(file_path)
        organizer.organize(file_path, code_data)
    
    # Optionally, display or save the organized data
    organizer.display()

if __name__ == "__main__":
    main()