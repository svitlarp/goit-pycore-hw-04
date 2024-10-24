import functools
import re
from os import stat


def to_str(bytes_or_str):
    '''Helper function takes a bytes or str instance and always return a str'''

    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value        


def total_salary(path: str) -> (int, int):
    """
    This function parses a text file with salary data of employees 
    and returns the total and average salary of all developers.
    Each line in the file contains the developer's last name and salary, 
    separated by a comma with no spaces.

    Parameters:
    path (str): The path to the text file

    Returns:
    (tuple) A tuple of two numbers: total salary and average salary.
    """
    try:
        #Check if the file is empty 
        if stat(path).st_size == 0:
            # raise Exception("File is empty")
            return "File is empty"

        else:
            with open(path, "r", encoding='utf-8') as file_obj:

                list_salary = []
                for line in file_obj.readlines():

                    # Ensure that data will be a str instance
                    to_str(line)

                    # Var to check if there are any numbers in the line to be able to perform mathematical operations on them.
                    contain_digits = bool(re.search(r"\d+", line))
                                     
                    if contain_digits is True:

                        # Using split() method extract salary data to perform math operations
                        file_data = line.split(',')
                        salary = int(file_data[-1].strip('\n '))
                        list_salary.append(salary)        

                    else:
                        return f'The salary should be written in numbers.'  
                        # raise Exception("The salary should be written in numbers.")

                if len(list_salary) > 1:
                    total_salary = functools.reduce(lambda x, y: x + y, list_salary) # sum(list_salary))
                    average_salary = total_salary // len(list_salary)
                else:
                    return f'The salary is {list_salary[0]}. File contains only one row' 
                    # raise Exception(f'The salary is {list_salary[0]}. File contains only one row')

                return (total_salary, average_salary)

    except FileNotFoundError:
        return "File does not exist"

file_one = "/home/unixsv/python_module_goit/goit-pycore-hw-04/file_one.txt" # (total_salary, average_salary)
file_two = "test2.ftp"  # file does not exist
file_three = "/home/unixsv/python_module_goit/goit-pycore-hw-04/test-files-for-task1/file_three.txt" # file with wrong data: numbers are written out in words.
file_four = "/home/unixsv/python_module_goit/goit-pycore-hw-04/test-files-for-task1/file_four.txt" # with only one line of text
file_five = "/home/unixsv/python_module_goit/goit-pycore-hw-04/test-files-for-task1/file_five.txt" # empty file
file_six = "/home/unixsv/python_module_goit/goit-pycore-hw-04/test-files-for-task1/file_six.exe" # file with binary data

print('file_1 result:', total_salary(file_one))
print('file_2 result:', total_salary(file_two))
print('file_3 result:', total_salary(file_three)) 
print('file_4 result:', total_salary(file_four))
print('file_5 result:', total_salary(file_five))
print('file_6 result:', total_salary(file_six))

# TestCase1 file with correct data (should find and return total_salary and average_salary)
assert total_salary(file_one) == (6000, 2000), "Test case 1 failed"

# TestCase2 file wich does not exist (should )
assert total_salary(file_two) == "File does not exist", "Test case 2 failed"

# TestCase3 file with data in wrong format: salary is written out in words.
assert total_salary(file_three) == 'The salary should be written in numbers.', "Test case 3 failed"

# TestCase4 file with only one line of text
assert total_salary(file_four) == 'The salary is 7000. File contains only one row', "Test case 4 failed"

# TestCase5 file is empty
assert total_salary(file_five) == "File is empty",  "Test case 5 failed"

# TestCase6 file with binary data
assert total_salary(file_six) == (5000, 2500),  "Test case 6 failed"
