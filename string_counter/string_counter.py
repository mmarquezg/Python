def string_counter(string):
    string = string.replace(' ', '')
    box_with_letters = []
    for i in string:
        box_with_letters.append(i)
    print(len(box_with_letters))


def run():
    string: str = input('Please insert a word or phrase: ')
    string_counter(string)


if __name__ == '__main__':
    run()
