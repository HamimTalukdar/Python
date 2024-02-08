'''Using the with Statement (Context Manager):'''

# The with statement ensures that the file is properly closed after the operations are performed.
with open('student.txt', 'r') as file:
    content = file.read()
    # File is automatically closed when the block is exited

print(content)