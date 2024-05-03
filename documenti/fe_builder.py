import shutil
import os

def copy_directory():
    # Ensure the source directory exists
    src_path= os.getcwd()+"/gemi"
    
    if not os.path.exists(src_path):
        print(f"The source directory {src_path} does not exist.")
        return

    # Get the parent directory
    parent_dir = os.path.dirname(src_path)
    parent_dir = os.path.dirname(parent_dir)

    # Get the base name of the source directory
    base_name = os.path.basename(src_path)

    # Create the destination path
    dst_path = os.path.join(parent_dir, base_name)

    # Copy the directory
    shutil.copytree(src_path, dst_path)

    print(f"Copied directory {src_path} to {dst_path}")