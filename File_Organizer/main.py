import os
import shutil

# Folder paths you want to organize
FOLDER_PATHS = os.getcwd()  # Current working directory

# Define file type categories and their corresponding extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".js", ".html", ".css"],
    "Others": []  # For files that don't match any category 
}

def organize_files(folder_path):
    # Create category folders if they don't exist
    for category in FILE_CATEGORIES.keys():
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)

        # Determine the category for the file
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension.lower() in extensions:
                shutil.move(file_path, os.path.join(folder_path, category, filename))
                moved = True
                break

        # If the file doesn't match any category, move it to "Others"
        if not moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", filename))

if __name__ == "__main__": 
    organize_files(FOLDER_PATHS)
    print("Files have been organized successfully.")

