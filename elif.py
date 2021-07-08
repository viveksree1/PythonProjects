n = int(6)
if 1 <= n <= 100:
    if ((2 <= n <= 5) or (n > 20)) and (n % 2 == 0):
        print("Not Weird")
    else:
        print("Weird")
