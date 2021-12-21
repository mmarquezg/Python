def palindrome(string):
    return string.lower().replace(' ', '') == string.lower().replace(' ', '')[::-1]

def palindrome_counter(string):
    string = string.split(' ')
    print(string)
    palindrome_words = [i for i in string if palindrome(i) == True]
    print('Amount of Palindrome: ' + str(len(palindrome_words)))

def run():
    string: str = input('Insert a phrase: ')
    palindrome_counter(string)



if __name__ == '__main__':
    run()