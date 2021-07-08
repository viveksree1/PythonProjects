a = raw_input("Enter a string:")
t = ""
res = ""
for i in range(0, len(a)):
    if a[i] == " ":
        res = t + " " + res
        t = ""
    else:
        t += a[i]
if (res == ""):
    res = t;
else:
    res = t + " " + res;
print res
b = (a.split(' '))
print(a.split(' '))

b = a.encode();
print(b)

############### SET 2 ################
#print('These values will be printed, {0}, {2}, {}'.format('a', 'b', 'c'))

sample_text = "Hello"
if type(sample_text) == str:
    print('Type of variable is string')
