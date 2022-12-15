from print_result import print_result

@print_result
def field(items, *args):
    assert len(args) > 0

    for item in items:
        tmp_res = {}

        if len(args) > 1:
            for arg in args:
                tmp_res[arg] = item[arg]
            yield tmp_res
        else:
            yield item[args[0]]
   

