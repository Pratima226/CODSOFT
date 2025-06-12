def calculator():
    print("=== Simple Calculator ===")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("⚠️ Please enter valid numbers!")
        return

    print("\nChoose Operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        result = num1 + num2
        op = '+'
    elif choice == '2':
        result = num1 - num2
        op = '-'
    elif choice == '3':
        result = num1 * num2
        op = '*'
    elif choice == '4':
        if num2 == 0:
            print("⚠️ Cannot divide by zero.")
            return
        result = num1 / num2
        op = '/'
    else:
        print("⚠️ Invalid choice.")
        return

    print(f"\nResult: {num1} {op} {num2} = {result}")


# Run the calculator
calculator()
