import shutil
import os

def copy_directory(src_path):
    # Ensure the source directory exists
    if not os.path.exists(src_path):
        print(f"The source directory {src_path} does not exist.")
        return
    
    # Get the parent directory
    parent_dir = os.path.dirname(src_path)

    # Get the base name of the source directory
    base_name = os.path.basename(src_path)

    # Create the destination path
    dst_path = os.path.join(parent_dir, base_name)

    # Copy the directory
    shutil.copytree(src_path, dst_path)

    print(f"Copied directory {src_path} to {dst_path}")