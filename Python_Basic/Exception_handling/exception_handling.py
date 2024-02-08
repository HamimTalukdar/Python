try:
    # Code that may raise an exception
    x = 10 / 0
except ZeroDivisionError as e:
    # Code to handle the specific exception (division by zero)
    print(f"Error: {e}")
except Exception as e:
    # Code to handle other types of exceptions
    print(f"Unexpected error: {e}")
else:
    # Code to execute if no exception occurs
    print("No exception occurred.")
finally:
    # Code that will be executed no matter what
    print("Finally block executed.")
