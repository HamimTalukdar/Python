try:
    # Code that may raise an exception
    num1 = int(input("Enter a numerator: "))
    num2 = int(input("Enter a denominator: "))
    result = num1 / num2

except (ValueError, ZeroDivisionError):
    print("You have entered incorrect input.")
    
else:
    # Code to execute if no exception occurs
    print(f"Result of division: {result}")

finally:
    # Code that will be executed no matter what
    print("Finally block executed.")
