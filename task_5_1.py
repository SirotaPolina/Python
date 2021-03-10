"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
"""


def uneven_numbers(number):
     yield from range(1, number, 2)


for i in uneven_numbers(30):
    print(i)
