"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
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
    print(numbers.get(number))


num_translate(eng_number)
