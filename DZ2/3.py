# 3) Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# Для n = 5: сумма = 11,55
import math
n = int(input("Введите число: "))
sum =0
for i in range(1,n+1):
    sum += pow((1+(1/i)),i)
print(f'Для n = {n}: сумма = {round(sum,2)}')