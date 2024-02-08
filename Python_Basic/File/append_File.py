# Opening a file in write mode
file = open('student.txt', 'a')
print(file.writable())

# Writing a string to the file
file.write(" I am ganna eat you. ")

file.close()
