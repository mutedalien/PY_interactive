x = int(input('Введите х: '))
if x > 0:
    y = 2 * x - 10
elif x == 0:
    y = 0
else:
    y = 2 * abs(x) - 1  # abs - функция, которая находит модуль числа
print(f'y = {y}')
