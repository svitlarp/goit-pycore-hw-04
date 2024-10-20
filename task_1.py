import functools
import re
from os import stat



# Helper function takes a bytes or str instance and always return a str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value        


# print(to_str(b'Alex Korp,3000'))
# Byte string to write

    

def total_salary(path):
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
        #Check if file is empty 
        if stat(path).st_size == 0:
            return "File is empty"

        else:
            with open(path, "r", encoding='utf-8') as file_obj:

                list_salary = []
                for line in file_obj.readlines():
                    print(type(line))

                    # Ensure that data will be a str instance
                    to_str(line)

                    # Var to check if there are any numbers in the line to be able to perform mathematical operations on them.
                    contein_digits = bool(re.search(r"\d+", line))
                    
                    # Using splt() method extract salary data to perform math operations
                    file_data = line.split(',')

                    if contein_digits is True:
                        salary = int(file_data[-1].strip('\n '))
                        list_salary.append(salary)                 
                    else:
                        result = line + "-> To calculate total salary and average salary salary should be written in numbers"
                        return result  

                total_salary = functools.reduce(lambda x, y: x + y, list_salary)
                average_salary = total_salary//len(list_salary)
                return (total_salary, average_salary)

    except FileNotFoundError:
        return "File does not exist"

file_one = "file_one.txt" # (total_salary, average_salary)
file_two = "test2.ftp"  # file does not exist
file_three = "file_three.txt" # file with wrong data: numbers are written out in words.
file_four = "file_four.txt" # with only one line of text
file_five = "file_five.txt" # empty file
file_six = "file_six.exe" # file with binary data

print('file_1 result:', total_salary('file_one.txt'))
print('file_2 result:', total_salary(file_two))
print('file_3 result:', total_salary(file_three)) 
print('file_4 result:', total_salary(file_four))
print('file_5 result:', total_salary(file_five))
print('file_6 result:', total_salary(file_six))

# TestCase1 file with correct data (should find and return total_salary and average_salary)
assert total_salary(file_one) == (6000, 2000), "Test case 1 failed"

# TestCase2 file wich does not exist (should )
assert total_salary(file_two) == "File does not exist", "Test case 2 failed"

# TestCase3 file with data in wring format: salary is written out in words.(should return )
assert total_salary(file_three) == '''Alex Korp,three hundred
-> To calculate total salary and average salary salary should be written in numbers'''

# # TestCase4 file with only one line of text
# assert total_salary(file_four) == '''It is not necessary to calculate the total and average salary 
                                    # since the file contains only one line''',  "Test case 4 failed"

# TestCase5 file is empty
assert total_salary(file_five) == "File is empty",  "Test case 5 failed"

# # TestCase6 file with binary data
assert total_salary(file_six) == (5000, 2500),  "Test case 6 failed"


# Create file 'file_six.exe' with binary data
# binary_data = b'Alex Korp,3000\nNikita Borisenko,2000'

# # Write to a binary file
# with open('file_six.exe', 'wb') as file:
#     file.write(binary_data)



# # Create files with data
# employee_data = ("Alex Korp,3000 \n"
#         "Nikita Borisenko,2000 \n"
#         "Sitarama Raju,1000")

# def create_files(num, data):
#     if isinstance(num, int) and num:
#         filename = 'file_0'
#         for i in range(1, 6):
#             with open(filename, "w") as file:
#                 file.writelines(data)
#             filename = filename[:-1] + str(i)
#     else:
#         print('Parameter `num` should be an integer to be able to create range of files')        

# create_files(4, employee_data)
            