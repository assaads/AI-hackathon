import os

def generate_combined_file(codebase_directory):

    # Initialize an empty string to store the combined content
    combined_content = ""

    # Traverse the codebase directory
    for root, _, files in os.walk(codebase_directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Open each file and append its contents to the combined content string
        try:
            with open(file_path, 'r', encoding='ISO-8859-1') as input_file:
                combined_content += f"\n\n# File: {file_path}\n\n"
                combined_content += input_file.read()
        except Exception as e:
            print(f"Could not read file {file_path}. Error: {e}")


    # Count the number of lines in the combined output
    num_lines = combined_content.count('\n')

    # Check if the number of lines exceeds the limit
    if num_lines >= 29000:
        raise ValueError(f"The combined output of the codebase has {num_lines} lines, which exceeds the limit of 29000 lines.")

    # # Write the combined content into the output file
    # with open(output_file_path, 'w', encoding='ISO-8859-1') as output_file:
    #     output_file.write(combined_content)

    # print(f"All files in {codebase_directory} have been written to {output_file_path}.")
    
    # Return the combined content
    return combined_content