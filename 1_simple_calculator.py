# -*- coding: utf-8 -*-
"""1.Simple calculator

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Bvh-0FCexzN-0AuSYkrlw0CCuBoZn5Nv
"""

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice(1/2/3/4): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '1':
   print(f"The result is: {num1 + num2}")
elif choice == '2':
   print(f"The result is: {num1 - num2}")
elif choice == '3':
   print(f"The result is: {num1 * num2}")
elif choice == '4':
   print(f"The result is: {num1 / num2}")
else:
   print("Invalid input")

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
print("Sum:" , x + y)
print("Subtraction:" , x - y)
print("Multiplication:" , x * y)
print("Division:" , x / y)