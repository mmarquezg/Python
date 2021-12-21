def piglatin(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0] in vowels:
        word = word + 'air'
    else:
        word = word[1:len(word)] + word[0] + 'ay'
    print(word)


def run():
    piglatin(input('Insert a word: '))


if __name__ == '__main__':
    run()