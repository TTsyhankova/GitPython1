#exe.3 Програма для визначення числа
n=int(input("Enter number: "))
if n == 0:
    print("Number is equal to zero")
elif n > 0: # Позитивне число
    print("Number is positive")
else: # Від'ємне число
    print("Number is negative")