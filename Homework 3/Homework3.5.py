a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# First way
result = []
for i in a:
    if i in result:
        continue
    for j in b:
        if i == j:
            result.append(i)
print(result)
# Second way
result_2 = list(set(a) & set(b))
print(result_2)