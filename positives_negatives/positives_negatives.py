def positives_negatives(number):
    if number > 0:
        print('Your number is positive')
    elif number < 0:
        print('Your number is negative')
    elif number == 0:
        print('Your number is zero')


def run():
    while True:
        try:
            number: int = int(input('Mario, please insert a number: '))
            positives_negatives(number)
            return False
        except ValueError:
            print('You must insert a number')


if __name__ == '__main__':
    run()
