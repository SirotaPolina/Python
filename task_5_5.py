"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [el for el in src if src.count(el) == 1]
print(result)

"""
result_test = list(filter(lambda x: src.count(x) == 1, src))
print(result_test)
"""