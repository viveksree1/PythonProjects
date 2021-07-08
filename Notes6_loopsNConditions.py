flag=True
if flag:
    print ("condition is True")

k="String here"
for c in k:
    print(c)


d = {'k1':1,'k2':2}
for item in d:
    print(item)
for item in d.items():
    print(item)
for value in d.values():
    print(value)


######## WHILE ############
x=0
while x<5:
    x+=1
#while with else:
x=50
while x<5:
    x+=1
else:
    print ("X is greater than 5")

####  PASS ####

for item in k:
    pass;
   # break;
  #  continue;

###################
#prints in the range 2 to 9 wuth break of 2
for num in range(2,10,2):
    print(num)

######### Prints  character and index as tuple ########
for c in enumerate(k):
    print(c)
#more clearly:
for c,i in enumerate(k):
    print(c)
    print(i)
