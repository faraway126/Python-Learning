import random
print('Добро пожаловать в числовую угадайку!')
number=random.randint(1, 100)
def is_valid(number):
    if 1<=number<=100:
        return True
    else:
        return False
def input_digit():
    while True:
        print('Введите число от 1 до 100')
        digit=input()
        if is_valid(int(digit)):
            return int(digit)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            
def ugaday_main():
    while True:
        digit=input_digit()
        if digit<number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif digit>number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break

ugaday_main()    

