def func1(l,l2):
    for i in l:
        print(type(i))
        if (type(i) == list):
            func1(i, l2)
        else:
            l2.append(i)
    return l2

l=[1,2,['a','b',['cat','dog'],'c'],3]
print(l)
#print(l[2][2][0][2])
l2=[]
l2=func1(l,l2)
print(l2)