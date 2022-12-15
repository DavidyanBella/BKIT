m class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self._data = items
        self._ignore_case = kwargs['ignore_case'] if 'ignore_case' in kwargs.keys() else False

    # Unique([1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) -> [1, 2]
    def __next__(self):
        result = []
        for elem in self._data:
            elem = elem.lower() if type(elem) == str and self._ignore_case else elem
            if elem not in result:
                result.append(elem)
        return result

    def __iter__(self):
        return self
