adding_names = True
filename = 'guest_book.txt'
prompt = "What's your name?\n"
prompt += "(enter 'quit' to stop adding names)\n"

while adding_names:
    name = input(prompt)
    if name == "quit":
        adding_names = False
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")


print("Thank you for signing our guest book!")
