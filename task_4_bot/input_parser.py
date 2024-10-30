import re


def parse_input(text: str):
    # розбиратиме введений користувачем рядок на команду та її аргументи
    # "add John 1234567890"
    if isinstance(text, str) and text:
        text = text.lower()

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


user_input = input('Enter what you wonna do with your phone_book:  ')
response_action, *given_args = parse_input(user_input)
print('response action: ', response_action)
print('given arguments: ', given_args)


def change_contact(name, phone_to_update):
    phone_book = {'bob':'9999'}
    if name in phone_book:
        phone_book[name] = phone_to_update
        return "Contact updated."
    else:
        raise NameDoestNotExists()


name, phone = given_args
print(change_contact(name, phone))

