# ZIP and get a combined tuple:

l1=[1,2,3,4]
l2=['a','b','c','d', 'e']

zip(l1,l2)

for item in zip(l1,l2):
    print(item)

# use in to check an element in list
print('x' in l2)

# min , max

print (min(l1))
print (max(l1))

# IMPORT

from random import shuffle
l3=[1,2,3,4,5,6,7,8,9]
shuffle(l3)
print(l3)

from random import randint
print(randint(0,100))

# GET INPUT

ip = str(raw_input("Enter a name here:"))
print(ip)
print ("The name is {}".format(ip))

# Make a list easier
listV= [c for c in "Vivek"]
print(listV)

listV= [x**2 for x in range(0,11)]
print(listV)

# complex aritematic

celcius = [0,1,10,20.5]
farenheit = [((9/5)*temp + 32) for temp in celcius]
print(farenheit)


def method_name():
    listV = [x ** 2 for x in range(0, 11) if x % 2 == 0]
    return listV


listV = method_name()
print(listV)
 #also this:
listV= [x**2 if x%2==0 else 'ODD' for x in range(0,11)]
print(listV)ne

from kafka import K