import re


# На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям, 
# змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг. 


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




def main():
    phone_book = {}
    print(MENU)

    print('hello')
    print('"How can I help you?"')
    # # управляє основним циклом обробки команд.
    # while input != "exit" and input != "close" :
    #     choice = input('Enter what you wonna do with your phone_book in this format: "add John 1234567890" ')
    #     match choice:
    #         case1:  



def add_contact(name: str, phone: str) -> str:
    if name not in phone_book:
        phone_book[name] = phone
        return "Contact added."
    else:
        raise NameError('''Can not add because this contact has already exists in phone book. 
                            Try change_contact to change it.''')


def change_contact(name, phone_to_update):
    if name in phone_book:
        phone_book[name] = phone_to_update
        return "Contact updated."
    else:
        raise NameError('No such name in phone_book')
    

def show_phone(name):
    if name in phone_book:
        return phone_book[name]
    else:
        raise NameError('No such name in phone_book')
    

def show_all():
    return phone_book











