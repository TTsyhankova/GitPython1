#exe.3 Програма для визначення числа

print("Exercise №3")

n=int(input("Enter number: ")) # Введіть число
if n == 0:
    print("Number is equal to zero") # Число дорівнює нулю
elif n > 0: # Позитивне число
    print("Number is positive") # Позитивне число
else: # Від'ємне число
    print("Number is negative") # Негативне число