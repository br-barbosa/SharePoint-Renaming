# Filename search_and_rename.py

This Python script is designed to clean up filenames and folder names within a specified directory. It removes unwanted characters, including Unicode symbols, leading and trailing spaces, and a list of specified special characters. It also ensures filenames are unique to avoid conflicts.

## Features

- Removes Unicode characters from filenames.
- Removes leading and trailing spaces from filenames.
- Removes unwanted characters: `. , ~ # % & * { } \ : ; < > ? / | "`.
- Ensures filenames are unique within the directory.
- Preserves file extensions.

## Requirements

- Python 3.x

## Usage

1. Open the `search_and_rename.py` script in your favorite text editor.

2. Replace the following line with the path to your target directory:

    ```python
    directory_path = 'Z:\\Root' # Replace with your main folder path
    ```

3. Run the script:

    ```bash
    python search_and_rename.py
    ```

## Functionality

### normalize_filename(filename)

This function takes a filename as input and returns a normalized filename by performing the following operations:

- Splits the filename into base name and extension.
- Removes leading and trailing spaces from the base name.
- Removes Unicode characters from the base name.
- Removes unwanted characters from the base name.
- Replaces multiple spaces with a single space.
- Reassembles the filename with the extension.

### unique_filename(directory, filename)

This function ensures that the normalized filename is unique within the specified directory by appending a counter if necessary.

### rename_files_and_folders(directory)

This function traverses the specified directory, normalizes filenames for all files and directories, ensures the names are unique, and renames them.

## Example

Before running the script, a directory might contain files and folders like:

example .txt
exa.mple.txt
exa;mple.txt
ex~ample.txt
example#.txt
ex%ample.txt
example name.txt


After running the script, the filenames will be normalized:

example.txt
exampletxt
exampletxt
exampletxt
exampletxt
exampletxt
example name.txt

## License

This project is licensed under the MIT License.
