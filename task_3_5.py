"""
Реализовать функцию get_jokes(), возвращающую n шуток,
сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого).
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""
from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count, repeat):
    """Generate n jokes from 3 random words taken from three lists: nouns, adverbs, adjectives."""
    i = 0
    jokes = []
    while i < count:
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        joke = [noun, adverb, adjective]
        jokes.append(' '.join(joke))
        if repeat == 'Нет':
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
        i += 1
    print(jokes)


answer = input('Хотите ли вы, чтобы слова в шутках повторялись? Да или Нет? ').capitalize()
if answer == 'Да':
    number = int(input(f'Сколько шуток вы хотите придумать? '))
else:
    number = int(input(f'Сколько шуток вы хотите придумать от 1 до {len(nouns)}? '))

get_jokes(repeat=answer, count=number)
