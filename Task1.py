# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# *Пример:*
# - 6782 -> 23
# - 0.56 -> 11

def input_number(st):
    try:
        number = float(input(f"{st}"))
    except ValueError:
        print("Введен символ...")
        exit()
    return number

def sum_number(n):
    sum = 0
    for i in str(n):
        if i != '.':
            sum += int(i)
    return sum

num = input_number("Введите число: ")
print(sum_number(num))
