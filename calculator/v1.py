print(" Simple Calculator ")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


print("\nSelect operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter choice (1, 2, 3, or 4): ")


if choice == "1":
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == "2":
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif choice == "3":
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")

elif choice == "4":
    # Prevent division by zero
    if num2 == 0:
        print("\nError: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")

else:
    print("\nInvalid choice! Please choose 1, 2, 3, or 4.")