import sys
from pathlib import Path
# import colorama
# from colorama import Fore, Back, Style

# colorama.init(autoreset=True)
# print(Fore.MAGENTA + str(var))


# print(file_name)
# given_path = ('bdfb') 
# given_path = ('..') 
given_path = '../modul5_files'


def displaying_dir_content(directory):
    print(str(directory))

    path_obj = Path(directory)

    for file in path_obj.iterdir():
        # print(file)
        if file.is_dir():
            # relative_path = file.relative_to(directory)
            # print(f'    {relative_path}/')
            displaying_dir_content(file)
        else:
            relative_path = file.relative_to(directory)
            print(f'- {relative_path}')

print(displaying_dir_content(given_path))            




# def displaying_dir_content(path):
#     '''
#     a script that takes a directory path as a command line argument 
#     and visualizes the structure of that directory, 
#     displaying the names of all subdirectories and files.
#     '''
#     # Check if path is a string
#     if isinstance(path, str):
#     # TODO check якщо вказаний шлях не існує

#         path_obj = Path(path)

#         # Iterate through all files in the folder (and subfolders)
  


# print(displaying_dir_content(given_path))


