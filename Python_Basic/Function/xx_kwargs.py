'''**kwargs (double asterisks) is used to pass a variable number of keyword arguments (i.e., named arguments) to a function. It allows you to pass any number of key-value pairs to the function, and these pairs will be received as a dictionary.'''
def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(name="John", age=25, city="New York")
