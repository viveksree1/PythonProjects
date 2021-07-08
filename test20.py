from collections import OrderedDict

dict = {'abc':30, 'bcd': 10, 'jkl':40, 'cde': 40, 'def': 35, 'efg': 10, 'fgh': 50, 'ghi': 40, 'hij':23}
sortRes=sorted(dict.values())
res=OrderedDict()
count=0;
for val in sortRes:
    for k in dict.keys():
        if(count<=5):
            if(dict[k]==val):
                res[k]=dict[k]
                count+=1
                break
print(res)
print(dict)