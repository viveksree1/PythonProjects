a = {
    "I":1, "II":2, "III":3, "IV":4, "V":5, "VI":6, "VII":7, "VIII":8, "IX":9, "X":10

}
#print(a[1])

k=raw_input("Enter the Roman Value between 1 to 10:")
print("The Roman value is:")
s=a[k[0]];
#print(k[1:])
if(len(k)>1):
    s+=a[k[1:]]
##for i in k:
 #   s+=a[i]
print(s)
