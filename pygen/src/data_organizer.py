class DataOrganizer:
    def __init__(self):
        self.data = {}
    
    def organize(self, file_path, code_data):
        """Organize the extracted data by file and folder."""
        self.data[file_path] = code_data
    
    def display(self):
        """Display the organized data."""
        for file_path, code_data in self.data.items():
            print(f"{file_path}: Lines={code_data['num_lines']}, Functions={code_data['num_functions']}")