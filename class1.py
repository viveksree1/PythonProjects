limit = input("Enter the limit for factorial");
if limit == 0:
    print(1);
elif limit == 1:
    print(1);
else:
    f = 1;
    for i in range(2, limit+1):
        f = f * i;
    print(f);
