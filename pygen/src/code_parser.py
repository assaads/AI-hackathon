class CodeParser:
    def parse(self, file_path):
        """Parse the given file and extract relevant information."""
        with open(file_path, 'r') as file:
            content = file.read()
        
        # For simplicity, we'll just count the number of lines and functions
        lines = content.split('\n')
        num_lines = len(lines)
        num_functions = sum(1 for line in lines if line.strip().startswith('def '))
        
        return {
            'num_lines': num_lines,
            'num_functions': num_functions
        }