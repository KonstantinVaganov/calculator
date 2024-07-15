try:
    number1 = int(input('Введите число 1: '))
    action = (input('Выбрать один из вариантов +, -, *, / : ')).strip()
    number2 = int(input('Введите число 2: '))

    if action == '+':
        print(number1 + number2)
    elif action == '-':
        print(number1 - number2)
    elif action == '*':
        print(number1 * number2)
    elif action == '/':
        if number1 == 0 or number2 == 0:
            print("К сожалению на 0 нельзя делить.")
        else:
            print(number1 / number2)
    else:
        print('Надо выбрать один из вариантов: + - * /, попробуйте снова.')

except ValueError:
    print("Введенное значение недопустимо.")
