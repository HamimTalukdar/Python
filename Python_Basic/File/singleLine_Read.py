'''Opening a File:'''

# Opening a file in read mode
file = open('example.txt', 'r')
print(file.readable())


'''Reading from a File:'''

# Reading a single line from the file
line = file.readline()
print(line)

# size of file --> total character of the file
size = len(line)
print(size)

file.close()
