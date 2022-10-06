import sys
import math


def get_coef(index, prompt):
    """
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент биквадратного уравнения
    """

    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = float(sys.argv[index])
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()

        while type(coef_str) != float:
            try:
                coef_str = float(coef_str)
            except:
                print(prompt)
                coef_str = input()

    return coef_str


def add_root(root_t, result):
    """
    Добавление корней биквадратного уравнения

    Args:
        root_t (float): корень квадратного уравнение A*t^2 + B*t + C = 0
        result (list[float]): список корней

    Returns:
        list[float]: Список корней
    """

    if root_t == 0:
        result.append(0)

    if root_t > 0:
        root1 = math.sqrt(root_t)
        result.append(root1)
        result.append(-root1)

    return result


def get_roots(a, b, c):
    """
    Вычисление корней биквадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    """

    result = []

    D = b * b - 4 * a * c

    if D == 0.0:
        root_t = -b / (2.0 * a)
        result = add_root(root_t, result)

    elif D > 0.0:
        sqD = math.sqrt(D)

        root_t1 = (-b + sqD) / (2.0 * a)
        root_t2 = (-b - sqD) / (2.0 * a)

        result = add_root(root_t1, result)
        result = add_root(root_t2, result)

    return result


def main():
    """
    Основная функция
    """

    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {:.2f}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {:.2f} и {:.2f}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {:.2f}, {:.2f} и {:.2f}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {:.2f}, {:.2f}, {:.2f} и {:.2f}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
