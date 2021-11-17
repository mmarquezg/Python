def finding_duplicated(length: int):
#Generando la lista
    user_list = []
    list_length = 0
    while list_length < length:
        try:
            number: int = int(input('Please, insert a number for your list: '))
            user_list.append(number)
            list_length = len(user_list)
        except ValueError:
            print('Please, insert a number')
#Identificando los elementos repetidos
    duplicated = []
    not_duplicated = []
    for n in user_list:
        if n not in not_duplicated:
            not_duplicated.append(n)
        else:
            duplicated.append(n)
    if len(duplicated) == 0:
        print('There is no duplicated elements in your list')
    else:
        print('There are duplicated elements in your list, the first one is: ' + str(duplicated[0]))
    print('This is the list generated: ' + str(user_list))

def run():
    while True:
        try:
            user_length: int = int(input('List Lenght: '))
            finding_duplicated(user_length)
            return False
        except ValueError:
            print('Please, insert a number')


if __name__ == '__main__':
    run()
