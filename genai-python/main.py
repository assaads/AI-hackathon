import sys
from code_parser import CodeParser
from file_utils import list_files

def main():
    if len(sys.argv) != 2:
        print("Usage: main.py <path_to_codebase>")
        sys.exit(1)
    
    codebase_path = sys.argv[1]
    files = list_files(codebase_path)
    
    parser = CodeParser()
    for file_path in files:
        parser.parse_file(file_path)

if __name__ == "__main__":
    main()