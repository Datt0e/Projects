num = int(input("Input a number: "))
factorial = 1
iter_num = num 

if num == 0:
    print(f"The factorial of {num} is {factorial}.")
else:
    while iter_num > 0:
        factorial = factorial*iter_num
        iter_num -= 1
    else:
        print(f"The factorial of {num} is {factorial}")