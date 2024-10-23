import re


def parse_input(text: str):
    # розбиратиме введений користувачем рядок на команду та її аргументи
    # "add John 1234567890"
    if re.match(r'^add', text):
        method, name, phone = text.split()
        print(
            'method: ', method, '\n',
            'name:', name, '\n',
            'phone: ', phone
        )
        return method, name, phone
    elif re.match(r'^change', text):
        method, name, phone = text.split()
        print(
            'method: ', method, '\n',
            'name:', name, '\n',
            'phone: ', phone
        )
        return method, name, phone
    elif re.match(r'^phone', text):
        method, name = text.split()
        print(
            'method: ', method, '\n',
            'name:', name,
        )   
        return method, name     
    elif re.match(r'^all', text):
        method = text
        print('method: ', method)   
        return method  

print(parse_input("add John 1234567890"))

