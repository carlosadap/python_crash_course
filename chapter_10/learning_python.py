filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(contents)
print()

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

print()

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print()

for line in lines:
    message = line.replace('python', 'C')
    print(message.rstrip())



