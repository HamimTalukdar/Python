'''*args (single asterisk) is used to pass a variable number of non-keyword arguments to a function. It allows you to pass any number of arguments to the function, and these arguments will be received as a tuple.'''
def example_function(*args):
    for arg in args:
        print(arg)

example_function(1, 2, 3, "hello")
