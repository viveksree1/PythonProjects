def check_even_list(num_list):
    even_numbers = []
    print(num_list)
    i=0
    # Go through each number
    for number in num_list:
        i += 1
        print(i)
        # Once we get a "hit" on an even number, we append the even number
        if number % 2 == 0:
            even_numbers.append(number)
        # Don't do anything if its not even
        else:
            continue
            print("After continue")

    # Notice the indentation! This ensures we run through the entire for loop
    return even_numbers

print(check_even_list([1,2,3,4,5,6,7,8,9]));

print("tailer"[::-1])