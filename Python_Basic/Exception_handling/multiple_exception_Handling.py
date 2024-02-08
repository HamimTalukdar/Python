try:
    # Code that may raise an exception
    num1 = int(input("Enter a numerator: "))
    num2 = int(input("Enter a denominator: "))
    result = num1 / num2

except ValueError as ve:
    # Handle the case when the input is not a valid integer
    print(f"ValueError: {ve}")

except ZeroDivisionError as zde:
    # Handle the case when attempting to divide by zero
    print(f"ZeroDivisionError: {zde}")

except Exception as e:
    # Catch any other type of exception
    print(f"Unexpected error: {e}")

else:
    # Code to execute if no exception occurs
    print(f"Result of division: {result}")

finally:
    # Code that will be executed no matter what
    print("Finally block executed.")
