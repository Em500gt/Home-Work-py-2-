# Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint
import random
n = int(input("Введите число: "))

lst = []
lst_second =[]

for i in range(n):
    lst.append(i)

print(lst)

for i in range(n):
    r = random.randint(0, n - 1)
    temp = lst[i]
    lst[i] = lst[r]
    lst[r] = temp 

print(lst)