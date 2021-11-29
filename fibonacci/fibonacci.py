def fibonacci(number):
    n1: int = 0
    n2: int = 1
    counter: int = 0
    while counter < number:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux


def run():
    fibo_list = []
    number : int = int(input('Please insert a maximum number for Fibonacci Generator: '))
    assert number > 0;'You must insert a number bigger than zero (0)'
    fibo_number = fibonacci(number)
    while len(fibo_list) < number:
        for element in fibo_number:
            fibo_list.append(element)
    print('Fibonacci number: ' + str(fibo_list[number - 1]))


if __name__ == '__main__':
    run()