# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def stepen (n, power):
    if power == 0:
        return 1
    return n * stepen(n, power - 1)

n = int(input("Введите число: "))
power = int(input("Введите степень числа: "))

print (stepen(n, power))