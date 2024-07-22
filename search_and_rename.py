import os
import re

def normalize_filename(filename):
    # Split the filename into base name and extension
    base, ext = os.path.splitext(filename)
    
    # Remove leading and trailing spaces from the base name
    base = base.strip()
    
    # Remove unicode characters from base name
    base = ''.join(char for char in base if ord(char) < 128)
    
    # Define a regex pattern to match unwanted characters
    pattern = r'[.,~#%&*{}\\:;<>?/|"]'
    
    # Apply the regex pattern to remove unwanted characters, including periods
    base = re.sub(pattern, '', base)
    
    # Remove multiple spaces
    base = re.sub(r'\s+', ' ', base)
    
    # Reassemble the filename with the extension
    normalized_name = f"{base}{ext}"
    
    return normalized_name

def unique_filename(directory, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    
    return new_filename

def rename_files_and_folders(directory):
    for root, dirs, files in os.walk(directory):
        for name in files + dirs:
            current_path = os.path.join(root, name)
            normalized_name = normalize_filename(name)
            if normalized_name != name:
                new_name = unique_filename(root, normalized_name)
                normalized_path = os.path.join(root, new_name)
                try:
                    os.rename(current_path, normalized_path)
                    print(f'Renamed: {current_path} -> {normalized_path}')
                except PermissionError as e:
                    print(f"PermissionError: {e} - {current_path}")
                except FileExistsError as e:
                    print(f"FileExistsError: {e} - {current_path}")

if __name__ == '__main__':
    directory_path = 'Z:\\Root' # Replace with your main folder path
    rename_files_and_folders(directory_path)