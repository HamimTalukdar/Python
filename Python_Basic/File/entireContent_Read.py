'''Opening a File:'''

# Opening a file in read mode
file = open('example.txt', 'r')
print(file.readable())


'''Reading from a File:'''

# Reading the entire content of the file
content = file.read()
print(content)

# size of file --> total character of the file
size = len(content)
print(size)

# Closing a File
file.close()
