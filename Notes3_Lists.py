a = [1, 2, 3, 4, 5, 1, 2, 7, 8, 1, 2, 8, 1]
print(a)
p = 0
l = []
k = 0
for i in range(0, len(a)):
    if a[i] not in l:
        l.append(a[i])
        c = 1
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                c = c + 1
        if c > 0:
            p = p + (c / 2)
print('Result:{}'.format(p))
b = ['a',1]
print(b)
print(l)