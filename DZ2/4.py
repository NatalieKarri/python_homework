# 4) Задайте число N и создайте список, заполненный числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input("Введите число: "))
numbers = []
for i in range(-n,n+1):
    numbers.append(i)
print(numbers)

sum =1 
index = []
f = open('text.txt', 'r')
for line in f.readlines():
    sum *= numbers[int(line)]
    index.append(int(line))
print(f'Позиции {index}, Произведение равно {sum}')
