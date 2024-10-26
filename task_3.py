import sys
import colorama
from colorama import Fore, Back, Style
from pathlib import Path


def display_directory_content(path):
    """
    a script that takes a directory path as a command line argument 
    and visualizes the structure of that directory, 
    displaying the names of all subdirectories and files.
    """
    
    if not isinstance(path, str):
        raise TypeError("The provided path must be a string.")
    
    path_obj = Path(path)
    
    if not path_obj.exists():
        raise Exception('The path does not exists')
    
    if not path_obj.is_dir():
        raise Exception('The path is a file, not a directory') 
    
    print(f"{path_obj}/")
    handle_path(path_obj)


def handle_path(path_obj: Path):    

    # Prints out all files in the folder (and subfolders) within given directory

    for file in path_obj.iterdir():
        if file.is_dir():
            relative_path = file.relative_to(path_obj)
            print(f'\n\t {relative_path}/')
            handle_path(file)
        else:
            relative_path = file.relative_to(path_obj)
            print(Fore.MAGENTA + f'- {relative_path}')


def main():
    print('CLI ARGUMENTS:', sys.argv[1])
    directory_path = sys.argv[1]

    display_directory_content(directory_path)


if __name__ == "__main__":
    main()        


given_path = '../modul5_files'
given_path_1 = (789)       # not correct type     
given_path_2 = ('/some_dir/another_dir')   # path does not exists
given_path_3 = 'intro.py'     # path is a file


# TestCase1 Correct data (should display the names of all files in a given directory and subdirectories)
# assert displaying_dir_content(given_path_1) == "The type of given path is not correct", "Test case 1 failed"

# TestCase1 type of path is not string (should raise an Exception: TypeError )
assert display_directory_content(given_path_1) == "The type of given path is not correct", "Test case 1 failed"


# TestCase2 path does not exist (should raise an Exception: FileNotFoundError)
assert display_directory_content(given_path_2) == "The path does not exists", "Test case 2 failed"

# TestCase3 the path is a file, not directory (should raise an Exception: FileNotFoundError)
assert display_directory_content(given_path_3) == "", "Test case 3 failed"
 
