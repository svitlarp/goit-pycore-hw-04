from pathlib import Path


def get_cats_info(file_path: str) -> list[dict]:
    """ 
    This function reads a file and creates a list of dict where every dict contain info about one cat.
    The get_cats_info() function is designed to process a text file containing information about cats.
    Each record of the file corresponds to a specific cat and includes id, name and age of a cat separated by a comma.

    Parameters:
    path (str): Path to the file 

    Returns:
    (list of dictionaries) The list of dict where each dict represents one cat.
    """
    cats_list = []
    cats_keys = ['id' , 'name' , 'age']
    try:
        # Check if file is empty
        if Path(file_path).stat().st_size == 0:
            return 'File is empty'
            # raise Exception("File is empty")

        with open(file_path, "r", encoding='utf-8') as file_obj:

            for line in file_obj.readlines():

                # With handy split() method extract all values separatly by specifying a comma as a separator
                line_data = line.strip('\n').split(',')   

                # Line by line append a new dictionary to the list        
                cats_list.append({k:v for (k, v) in zip(cats_keys, line_data)})
            return cats_list

    except FileNotFoundError:
        return "File does not exist" 
        # raise FileNotFoundError('File does not exist')           


file_one = 'test-files-for-task2/cats.txt'
file_two = 'dog.ftp'
file_three = 'test-files-for-task2/cats_empty.txt'


print(get_cats_info('test-files-for-task2/cats.txt'))
# print(get_cats_info('cats_empty.txt'))

# TestCase1 file with correct data (should return the list of dict where each dict represents one cat)
assert get_cats_info(file_one) == [{'id': '60b90c1c13067a15887e1ae1', 'name': 'Tayson', 'age': '3'}, {'id': '60b90c2413067a15887e1ae2', 'name': 'Vika', 'age': '1'}, {'id': '60b90c2e13067a15887e1ae3', 'name': 'Barsik', 'age': '2'}, {'id': '60b90c3b13067a15887e1ae4', 'name': 'Simon', 'age': '12'}, {'id': '60b90c4613067a15887e1ae5', 'name': 'Tessi', 'age': '5'}], "Test case 1 failed"

# TestCase2 file does not exist (should )
assert get_cats_info(file_two) == "File does not exist", "Test case 2 failed"

# TestCase3 Empty file (should )
assert get_cats_info(file_three) == "File is empty", "Test case 3 failed"

