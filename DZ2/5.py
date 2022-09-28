# 5) Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)
# Без рандома не смогла придумать алгоритм
import random
numbers = list(map(int,input("Введите элементы через пробел ").split()))
print(numbers)
for i in range(0, len(numbers)):
    index = random.randint(0,len(numbers)-1)
    temp = numbers[i]
    numbers[i] = numbers[index]
    numbers[index] = temp
print(numbers)    
