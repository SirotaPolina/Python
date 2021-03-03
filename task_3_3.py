"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
"""
workers_name = input('Введите имена ваших сотрудников: ').split()


def thesaurus(names):
    workers = {}
    for name in names:
        if name[0] in workers:
            workers[name[0]] = [workers[name[0]]]
            workers[name[0]].append(name)
        else:
            workers[name[0]] = name

    print(workers)


thesaurus(workers_name)
