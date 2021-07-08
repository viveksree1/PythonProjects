f = open("/Users/viveksrikumar/Documents/tf", "r")
st = f.read()
l = st.split("\n")
print(len(l))
i = 0
for val in l:
    if type(val) == str :
        if val :
            print("The value before main condition is:" + val.split(" ")[0])
