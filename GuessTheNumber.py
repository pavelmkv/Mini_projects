from random import *

num = randint(1, 100)
print('Добро пожаловать в "угадай число"')


def is_valid(line):
    if not line.isdigit():
        return False
    return 1 <= int(line) <= 100


while True:
    number_input = input('Введите целое число от 1 до 100')
    if is_valid(number_input):
        number_input = int(number_input)
        if number_input == num:
            print('Вы угадали, поздравляем!')
            break

        elif number_input > num:
            print('Ваше число больше загаданного, попробуйте еще разок')

        elif number_input < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')

    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
