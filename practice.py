import shutil

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File copied successfully from '{source}' to '{destination}'")
    except FileNotFoundError:
        print(f"Error: The file '{source}' does not exist.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
source_file = "src.txt"  # Replace with your source file path
destination_file = "destination.txt"  # Replace with your destination file path
copy_file(source_file, destination_file)
