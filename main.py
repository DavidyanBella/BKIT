from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer_1 import Cm_timer_1
from lab_python_fp.cm_timer_2 import Cm_timer_2


from time import sleep


@print_result
def test1():
    return 1


@print_result
def test2():
    return 'iu5'


@print_result
def test3():
    return {'a': 1, 'b': 2}


@print_result
def test4():
    return [1, 2]


def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    # goods = [
    #     {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    #     {'title': 'Диван для отдыха', 'color': 'black'}
    # ]

    field(goods, "title")
    print()

    field(goods, "title", "price")
    print()

    field(goods, "title", "price", "color")
    # print(gen_random(5, 1, 3))
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    #print(Unique(data, ignore_case=True).__next__())
    #print(Unique(data).__next__())

    # print(Unique([1, 1, 1, 1, 1, 2, 2, 2, 2, 2]).__next__())
   
    #gen_random(5, 1, 3)
    #test1()
    #test2()
    #test3()
    #test4()
    # print(type({'a': 1, 'b': 2}) == dict)


    with Cm_timer_1() as cm_timer_1:
        sleep(2)
        print(cm_timer_1)

    with Cm_timer_2() as cm_timer_2:
        sleep(2)
        print(cm_timer_2)


if __name__ == "__main__":
    main()
