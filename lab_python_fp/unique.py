class Unique(object):
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
        print(self._ignore_case)
        result = []
        for elem in self._data:
            if type(elem) == str:
                if self._ignore_case:
                    print("str?:", type(elem) == str, self._ignore_case)
                    tmp_l = elem.lower()
                    tmp_u = elem.upper()
                    if elem not in result and tmp_l not in result and tmp_u not in result:
                        result.append(elem)
                elif not self._ignore_case:
                    print("here2")
                    if elem not in result:
                        result.append(elem)
            print(result)
        return result

    def __iter__(self):
        return self
