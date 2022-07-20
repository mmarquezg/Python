import random
import os
TITLE = '''
Welcome to the HANGMAN GAME!
________________

Guess the word:
'''
HANGMAN = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''','''
      +---+
      |   |
          |
          |
          |
          |
    ========='''
]

def clear(): #limpia pantallas
    if os.name == "nt":
        os.system("cls")
    else:
        os.system('clear')


def read_data(): #obteniendo palabras de data.txt
    data = []
    with open('./files/data.txt', 'r', encoding='utf-8') as f:
        data = [word.strip('\n') for word in f]

    dict_data = {key:value for key, value in enumerate(data)}
    return dict_data


def normalize(s): #eliminando los acentos de las palabras
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def run():
    dict_data = read_data()
    secret_word = dict_data.get(random.randint(1, len(dict_data) + 1))
    secret_word = normalize(secret_word).upper()

    player_word = ["-" for i in range(0, len(secret_word))]
    lifes = 6

    while lifes != 0:
        letter_word = False
        try:
            print(TITLE)
            print(player_word)
            print(''.join(player_word))
            print(HANGMAN[lifes])
            letter = input('\nPlease insert a letter: ').upper()
            clear()
            if letter.isnumeric() or len(letter) > 1 or len(letter) == 0:
                raise ValueError
            for i, letter_secret in enumerate(secret_word):
                if letter == letter_secret:
                    player_word[i] = letter
                    letter_word = True
            if letter_word == False:
                lifes -= 1
            if "".join(player_word) == secret_word:
                print('Welcome to the HANGMAN GAME')
                print('\nYou have won! The secret word was:\n')
                print(''.join(player_word))
                break
        except ValueError:
            if letter.isnumeric():
                print('\nYou cannot insert a number. Please insert a letter')
                lifes -= 1
            if len(letter) > 1:
                print('\nYou must insert only one letter')
                lifes -= 1
            if len(letter) == 0:
                print('\nYou must insert a letter')
                lifes -= 1

    if lifes == 0:
        print('Oh! :( You have lost! the word was:\n')
        print(secret_word)
        print(HANGMAN[0])


if __name__ == '__main__':
    run()
