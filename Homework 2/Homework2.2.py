a = int(input("Enter the first number    "))
b = int(input("Enter the first number    "))
c = int(input("Enter the first number    "))
if a > b and a > c:
    print(a, " largest number")
elif b > a and b > c:
    print(b, " largest number")
else:
    print(c, " largest number")