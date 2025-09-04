while True:
    try:
        inches = int(input("Enter length in inches (negative to quit): "))
        if inches < 0:
            print("Goodbye!")
            break
        centimeters = inches * 2.54
        print(f"{inches} inches is {centimeters:.2f} centimeters.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")