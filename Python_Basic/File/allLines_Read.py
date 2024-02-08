'''Opening a File:'''

# Opening a file in read mode
file = open('example.txt', 'r')
print(file.readable())


'''Reading from a File:'''

# Reading all lines into a list
lines = file.readlines()
print(lines)

# size of file --> total character of the file
size = len(lines)
print(size)

file.close()
