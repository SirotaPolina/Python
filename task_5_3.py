"""
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <class>).
Количество генерируемых кортежей не должно быть больше длины списка tutors.
Если в списке classes меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None)
"""
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(tutors) - len(classes) > 0:
    while len(tutors) != len(classes):
        classes.append(None)

gen_tuple = ((tutors[i], classes[i])  for i in range(len(tutors)))

print(type(gen_tuple))
for n in gen_tuple:
    print(n)
