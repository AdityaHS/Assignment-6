#Question-5
s = input("enter string-")
list = s.split('-')
x = sorted(list)
for i in range(0, len(x)-1):
    print(x[i], end="-")
print(x[len(x)-1])
