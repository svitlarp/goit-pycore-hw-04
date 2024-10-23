# Helper function takes a bytes or str instance and always return a str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value        


def get_cats_info(file_path):
    """ 
    This function read a file and create a list of dict  where every dict contain info about one cat.
    The get_cats_info() function is designed to process a text file containing information about cats.
    Each record of the file corresponds to a specific cat and includes id, name and age of a cat separated by a comma.

    Parameters:
    path (str): Path to the file 

    Returns:
    (list of dictionaries) The list of dict where each dict represents one cat.
    """
    cats_list = []
    print(cats_list)
    cats_keys = ['id' , 'name' , 'age']
    try:
        with open(file_path, "r", encoding='utf-8') as file_obj:
            # TODO Check if file is empty

            for line in file_obj.readlines():

                # With handly split() method extract all values separatly by specifying a comma as a separator
                line_data = line.strip('\n').split(',')   
                print(line_data)

                # Line by line append a new dictionary to the list        
                cats_list.append({k:v for (k, v) in zip(cats_keys, line_data)})
            return cats_list
    except FileNotFoundError:
        return "File does not exist"            


# print(get_cats_info('/home/unixsv/python_module_goit/goit-pycore-hw-04/cats.txt'))
print(get_cats_info('cats.txt'))


file_one = 'cats.txt'
file_two = 'rich.ftp'
file_three = 'cats3.txt'
file_four = 'cats4.txt'

# TestCase1 file with correct data (should find and return total_salary and average_salary)
assert get_cats_info(file_one) == [{'id': '60b90c1c13067a15887e1ae1', 'name': 'Tayson', 'age': '3'}, {'id': '60b90c2413067a15887e1ae2', 'name': 'Vika', 'age': '1'}, {'id': '60b90c2e13067a15887e1ae3', 'name': 'Barsik', 'age': '2'}, {'id': '60b90c3b13067a15887e1ae4', 'name': 'Simon', 'age': '12'}, {'id': '60b90c4613067a15887e1ae5', 'name': 'Tessi', 'age': '5'}], "Test case 1 failed"

# TestCase2 file wich does not exist (should )
assert get_cats_info(file_two) == "File does not exist", "Test case 2 failed"

# # TestCase3 Empty file (should )
# assert get_cats_info(file_three) == "File does not exist", "Test case 2 failed"

# # TestCase4 data problem (should )
# assert get_cats_info(file_four) == "File does not exist", "Test case 2 failed"





# d = {key:value for key in line_data for value in x} 
# d = {key:value for key in x for value in line_data} # Question: why works unexpected in dict comprehension?
# cats_list.append({k:v for (k, v) in zip(cats_keys, line_data)})



cats_data = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,560b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5"""


# with open("cats.txt", 'w') as file:
#     file.write(cats_data)