import sys
from pathlib import Path
import colorama
from colorama import Fore, Back, Style


def displaying_dir_content(path):
    '''
#     a script that takes a directory path as a command line argument 
#     and visualizes the structure of that directory, 
#     displaying the names of all subdirectories and files.
#     '''
    # Check if path is a string
    if isinstance(path, str):
        path_obj = Path(path)
        # Check if given path exists and if is a dir
        if path_obj.exists():
            print(f'{path_obj}/ ')
            # if is a correct path display all directory content
            handle_path(path_obj)   
        else:
            return 'no file'
    else:
        return 'not correct type'    



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
            




# print(file_name)
# given_path = ('bdfb') 
# given_path = ('..') 
# given_path = (789) 
given_path = '../modul5_files'
# given_path = 'modul5_files'
# given_path = 'intro.py' # if path is a file


print(displaying_dir_content(given_path))            



