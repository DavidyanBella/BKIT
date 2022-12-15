import random
from print_result import print_result

# @print_result
def gen_random(num_count, begin, end):
    return [random.randrange(begin, end) for _ in range(num_count)] if num_count > 1 else random.randrange(begin, end)

