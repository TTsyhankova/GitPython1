#exe.5 Програма порівняння двох чисел
n1=int(input("Enter number1: "))
n2=int(input("Enter number2: "))
if n1 < n2:
    print(n1, n2)
elif n1 > n2:
    print(n2, n1)
else:
    print("The numbers are equal to each other")