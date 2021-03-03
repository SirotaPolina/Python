"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
"""
eng_number = (input('Напишите любое число на английском языке от 1 до 10: '))


def num_translate(number):
    numbers = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if number.istitle():
        number = number.lower()
        new_number = numbers[number].capitalize()
        print(new_number)
    else:
        print(numbers[number])


num_translate(eng_number)