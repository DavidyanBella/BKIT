# a = [1, 2, 3]
# b = [1, 4, 9]

a = [1, 2, 3]

# 1 способ
res1 = [(elem, elem ** 2) for elem in a]
print(res1)

# 2 способ
res2 = list(map(lambda elem: (elem, elem ** 2), a))
print(res2)

# 3 способ
res3 = list(zip(a, [elem ** 2 for elem in a]))
print(res3)

# 4 способ
res4 = list(zip([elem for elem in a], [elem ** 2 for elem in a]))
print(res4)

