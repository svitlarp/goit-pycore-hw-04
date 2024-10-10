from pathlib import Path
import functools
import re

def total_salary(path):
    """
    This function parses a text file with salary data of employees and returns the total and average salary of all developers.
    Each line in the file contains the developer's last name and salary, separated by a comma with no spaces.

    Parameters:
    path (str): The path to the text file

    Returns:
    (tuple) A tuple of two numbers: total salary and average salary.
    """
    try:
        # TODO handle param path -> The path to the text file not file name
        with open(path, "r") as file_obj:
            list_salary = []

            for line in file_obj.readlines():
                # Var to check if there are any numbers in the line to be able to perform mathematical operations on them.
                contein_digits = bool(re.search(r"\d+", line))
                
                # Using splt() method extract salary data to perform math operations
                file_data = line.split(',')

                if contein_digits == True:
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

print('file_1 result:', total_salary(file_one))
print('file_2 result:', total_salary(file_two))
print('file_3 result:', total_salary(file_three)) 
print('file_4 result:', total_salary(file_four))

# TestCase1 file with correct data (should find and return total_salary and average_salary)
assert total_salary(file_one) == (6000, 2000), "Test case 1 failed"

# TestCase2 file wich does not exist (should )
assert total_salary(file_two) == "File does not exist", "Test case 2 failed"

# # TestCase3 file with data in wring format: salary is written out in words.(should return )
# # Question: How to write a test with dynamic data??: result = line + "-> To calculate total salary and average salary salary should be written in numbers"
# assert total_salary(file_three) == "To calculate total salary and average salary salary should be written in numbers", "Test case 3 failed"

# # TestCase4 file with only one line of text
# assert total_salary(file_four) == file.content,  "Test case 4 failed"



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



# TODO Case4: file_four = "file_four.txt" # with only one line of text
# if there are only one line of text -> We will not calculate either the total salary or the average salary. 

# Check if file contains more than one line.
# (If there are only one line -> We will not calculate either the total salary or the average salary - it makes no sence.) 
# lines_length = len(file_obj.readlines())
# print(lines_length)

# if lines_length <= 1:
#         print('blabla')
# else: 
            