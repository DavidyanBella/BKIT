def num_sort(data, rev=False):
    return sorted(data, key=int.__abs__, reverse=rev)


def num_lambda_sort(data, rev=False):
    return sorted(data, key=lambda elem: abs(elem), reverse=rev)


def sort(data, rev=False):
    return sorted(data, reverse=rev)
