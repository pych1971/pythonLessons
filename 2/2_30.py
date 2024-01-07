try:
    a1 = float(input('Введите первое число: '))
except ValueError:
    print('Необходимо ввести число!')
    a1 = float(input('Введите первое число: '))
z = input('Введите арифметический знак (+, -, *, /): ')
try:
    a2 = float(input('Введите первое число: '))
except ValueError:
    print('Необходимо ввести число!')
    a2 = float(input('Введите первое число: '))

if z == "+":
    print(f'{a1} + {a2} = {a1 + a2}')
elif z == '-':
    print(f'{a1} - {a2} = {a1 - a2}')
elif z == '*':
    print(f'{a1} * {a2} = {a1 * a2}')
elif z == '/':
    try:
        print(f'{a1} / {a2} = {a1 / a2}')
    except ZeroDivisionError:
        print(f'{a1} / {a2} = бесконечность')
else:
    print('Неправильно введённый арифметический знак!')
