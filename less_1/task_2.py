# Линейные алгоритмы

num = input("Введите трехзначное число: ")
num = int(num)
a = num // 100
b = num % 100 // 10
c = num % 10
summa = a + b + c
mult = a * b * c
print(f'Сумма = {summa}')
print(f'Произведение = {mult}')
