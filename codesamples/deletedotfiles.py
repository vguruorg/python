import os

def delete_files_starting_with_dot(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith('.'):
                file_path = os.path.join(dirpath, filename)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

# Change the directory to the desired location
directory_to_search = "."  # Current directory
delete_files_starting_with_dot(directory_to_search)
