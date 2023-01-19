import json

from cm_timer_1 import Cm_timer_1
from gen_random import gen_random
from print_result import print_result
from sort import sort
from unique import Unique


path = "/Users/mikhail/Documents/BKIT/Lab1/files/data_light.json"
path_to_write = "../files/tmp_res.json"


with open(path) as f:
    data = json.load(f)


def f1(arg):
    return sort(Unique([i["job-name"] for i in arg], ignore_case = True).__next__())


def f2(arg):
    return list(filter(lambda a: "программист" == a.split()[0].strip(), arg))


def f3(arg):
    return [item + " с опытом Python" for item in arg]


@print_result
def f4(arg):
    sals = [gen_random(1, 100000, 200000) for _ in range(len(arg))]
    res_list = list(zip(arg, sals)) 
    return [i[0] + ", с зарплатой " + str(i[1]) + " руб." for i in res_list]


if __name__ == "__main__":
    with Cm_timer_1():
        f4(f3(f2(f1(data))))        


# Доп задание:
# a = [1, 2, 3]
# b = [1, 4, 9]
# 4 способа a -> b
