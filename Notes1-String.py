a = 3.5
print(type(a))
if type(9) is int:
    print("Its float")
a=144
math.sqrt(a)

################# STRINGS ##############

print("I 'm  going on run ")

print(len("VIVEK"))

#########################
a = raw_input("Enter a string:")
print(a)
t = ""
res = ""
for i in (0, len(a)-1):
    if a[i] == " " or i == len(a):
        print (t)
        res = t + res
        t = ""
    else:
        t += a[i]
print res

#################################################
