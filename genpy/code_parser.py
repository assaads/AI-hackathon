import os

def generate_combined_file(codebase_directory):
    # Define the codebase and output file paths
    # codebase_directory = input("Enter the path to the codebase directory: ")
    output_file_path = input("Enter the path to the output file: ")
    output_file_path = os.path.join(output_file_path, 'codebase_output.txt')
    # output_file_path = codebase_directory

    # Initialize an empty string to store the combined content
    combined_content = ""

    # Traverse the codebase directory
    for root, _, files in os.walk(codebase_directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Open each file and append its contents to the combined content string
            with open(file_path, 'r', encoding='ISO-8859-1') as input_file:
                combined_content += f"\n\n# File: {file_path}\n\n"
                combined_content += input_file.read()

    # Count the number of lines in the combined output
    num_lines = combined_content.count('\n')

    # Check if the number of lines exceeds the limit
    if num_lines >= 29000:
        raise ValueError(f"The combined output of the codebase has {num_lines} lines, which exceeds the limit of 29000 lines.")

    # Write the combined content into the output file
    with open(output_file_path, 'w', encoding='ISO-8859-1') as output_file:
        output_file.write(combined_content)

    print(f"All files in {codebase_directory} have been written to {output_file_path}.")
    
    # Return the combined content
    return combined_content