import shutil
import os
import sys

if len(sys.argv) != 3:
    print("Usage: python sync-config.py <source_path> <target_folder>")
    sys.exit(1)

source_path = os.path.expanduser(sys.argv[1])
target_folder = os.path.expanduser(sys.argv[2])

# Constructing the target path
target_path = os.path.join(target_folder, os.path.basename(source_path))

# Check if the target file or folder already exists
if os.path.exists(target_path):
    print(f"File or folder already exists in '{target_folder}'.")
    answer = input("Continue? (y/n): ")
    if answer.lower() != "y":
        print("Operation canceled.")
        sys.exit(0)

# Copying the file or folder, overwriting if it already exists
if os.path.isdir(source_path):
    shutil.copytree(source_path, target_path)
else:
    shutil.copy2(source_path, target_path)

print(f"Copied {source_path} to {target_folder}")
