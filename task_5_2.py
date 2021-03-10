"""
Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""

number = int(input('Введите любое число: '))
uneven_numbers = (num for num in range(1, number, 2))
for i in uneven_numbers:
    print(i)