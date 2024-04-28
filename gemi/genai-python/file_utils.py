import os

def list_files(directory):
    return [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in filenames if os.path.isfile(os.path.join(dp, f))]

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1][1:]  # Remove the dot from the extension