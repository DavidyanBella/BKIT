from operator import itemgetter

class Mic:
    def __init__(self, mic_id, name, summ, comp_id):
        self.mic_id = id
        self.name = name
        self.summ = summ
        self.comp_id = comp_id

class Comp:
    def __init__(self, id, namecomp):
        self.id = id
        self.namecomp = namecomp

class MicComp:
    def __init__(self, comp_id, mic_id):
        self.comp_id = comp_id
        self.mic_id = mic_id


mics = [
    Mic(1, 'Mic1', 25, 1),
    Mic(2, 'Moc2', 35, 2),
    Mic(3, 'Mic3', 45, 3),

    Mic(11, 'Moc1(1)', 35, 3),
    Mic(22, 'Mic2(2)', 25, 3),
    Mic(33, 'Mic3(3)', 15, 2),
]

comps = [
    Comp(1, 'A'),
    Comp(2, 'F'),
    Comp(3, 'D'),
    Comp(4, 'G'),
    Comp(5, 'H'),
]

mics_comps = [
    MicComp(1, 1),
    MicComp(2, 2),
    MicComp(3, 3),
    MicComp(3, 4),
    MicComp(3, 5),

    MicComp(11, 1),
    MicComp(22, 2),
    MicComp(33, 3),
    MicComp(33, 4),
    MicComp(33, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(e.name, e.summ, d.namecomp)
                   for d in comps
                   for e in mics
                   if e.comp_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.namecomp, ed.comp_id, ed.mic_id)
                         for d in comps
                         for ed in mics_comps
                         if d.id == ed.comp_id]

    many_to_many = [(e.name, e.summ, comp_name)
                    for comp_name, comp_id, mic_id in many_to_many_temp
                    for e in mics if e.mic_id == mic_id]

    print('Задание Б1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание Б2')
    res_12_unsorted = []
    # Перебираем все компьтеры
    for d in comps:
        # Список компьютеров
        d_mics = list(filter(lambda i: i[2] == d.namecomp, one_to_many))
        if len(d_mics) > 0:
            d_sums = [summ for _,summ, _ in d_mics]
            d_sums_sum = sum(d_sums)
            res_12_unsorted.append((d.namecomp, d_sums_sum))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание Б3')
    res_13 = {}
    # Перебираем все отделы
    for d in comps:
        if 'Moc' in d.namecomp:
            # Список сотрудников отдела
            d_mics = list(filter(lambda i: i[2] == d.namecomp, many_to_many))
            # Только ФИО сотрудников
            d_mics_names = [x for x, _, _ in d_mics]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[d.namecomp] = d_mics_names

    print(res_13)

    list_a = list(range(1, 4))
    list_a1 = [(i**2 for i in list_a)]
    list_b = [(x, y) for x in list_a for y in list_a1]
    print('\n\n', list_b)

    list_b = [(x, y**2) for x in list_a for y in list_a]
    print('\n\n', list_b)

    list_b = [[y for y in x] for x in list_a]
    print('\n\n', list_b)



if __name__ == '__main__':
    main()

# есть список А 123 получить список Б кортежных пар с помощью функ возм питона
