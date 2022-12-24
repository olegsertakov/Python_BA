number_max = input('Введите целое число: ')
number = number_max
i = 1
summa = 0
while i <= int(number_max):

    number = int(str(number_max) * i)
    print(number)
    summa = summa + number
    print('текущая сумма чисел = ', summa)
    i += 1
print('сумма ', number_max, 'чисел = ', summa)