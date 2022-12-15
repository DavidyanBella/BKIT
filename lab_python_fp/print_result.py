from types import GeneratorType


def print_result(function_to_decorate):
    """

    :rtype: object
    """
    def decorated_func(*args):
        # print("start")
        result = function_to_decorate(*args)
        if type(result) == dict:
            for item in result:
                print(item, "=", result[item])
        elif type(result) == list or type(result) == GeneratorType:
            for item in result:
                print(item)
        else: print(result)
        # print("end")

    return decorated_func
