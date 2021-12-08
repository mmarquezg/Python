def binary(number):
    binary_list = []
    while number != 0:
        rest = number % 2
        quotient = number // 2
        binary_list.append(str(rest))
        number = quotient
    binary_list = binary_list[::-1]
    binary_number = ''.join(binary_list)
    print(binary_number)


def run():
    number: int = int(input('Insert a number: '))
    binary(number)


if __name__ == '__main__':
    run()