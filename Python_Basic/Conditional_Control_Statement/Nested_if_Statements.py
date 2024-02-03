'''You can also nest if statements to check multiple conditions in a hierarchical manner.'''

a = 12

if a > 10:
    if a % 2 == 0:
        print("a is greater than 10 and even")
    else:
        print("a is greater than 10 but odd")
else:
    print("a is not greater than 10")
