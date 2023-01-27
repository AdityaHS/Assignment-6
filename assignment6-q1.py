#Question-1
a = int(input("Enter a number\n"))

def func(x):
    sum = 0

    for i in range(1, x):
        if (a%i==0):
            sum = sum + i
        else:
            pass

    if (sum==a):
        print(f"{x} is a perfect number")
    else:
        print(f"{x} is not a perfect number")

func(a)