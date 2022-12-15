#def sort(data, reverse=False):
#    for i in range(len(data)):
#        minimum = i
#
#        for j in range(i + 1, len(data)):
#            if data[j] < data[minimum]:
#               minimum = j
#
#       data[minimum], data[i] = data[i], data[minimum]
#   return data[::-1] if reverse else data

def num_sort(data, rev=False):
    return sorted(data, key=int.__abs__, reverse=rev)

def num_lambda_sort(data, rev=False):
    return sorted(data, key=lambda elem: abs(elem), reverse=rev)

def sort(data, rev=False):
    return sorted(data, reverse=rev)
