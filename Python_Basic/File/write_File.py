# Opening a file in write mode
file = open('student.txt', 'w')
print(file.writable())

# Writing a string to the file
file.write("Hello, this is a student text.")

file.close()
