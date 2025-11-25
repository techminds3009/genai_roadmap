import os

def add_gitkeep_to_empty_dirs(base_path):
    """
    Recursively traverse the directory structure and add a .gitkeep file
    to all empty directories.
    """
    for root, dirs, files in os.walk(base_path):
        # If a directory has no files and no subdirectories, it's empty
        if not dirs and not files:
            gitkeep_path = os.path.join(root, ".gitkeep")
            with open(gitkeep_path, "w") as f:
                pass  # Create an empty .gitkeep file
            print(f"Added .gitkeep to: {gitkeep_path}")

if __name__ == "__main__":
    # Set the base directory to the current working directory
    base_directory = os.getcwd()
    add_gitkeep_to_empty_dirs(base_directory)