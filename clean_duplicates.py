import os

# This script checks a folder and removes duplicate files based on name and size.
# I made this while learning how to handle files and automate small cleanup tasks.

def remove_duplicates(folder_path):
    seen = {}
    removed = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            key = (file, size)
            if key in seen:
                os.remove(path)
                removed += 1
                print(f"Removed duplicate: {path}")
            else:
                seen[key] = path
    print(f"Finished. Removed {removed} duplicate files.")

if __name__ == "__main__":
    folder = input("Enter the folder path to check: ").strip()
    if os.path.isdir(folder):
        remove_duplicates(folder)
    else:
        print("Folder not found.")
