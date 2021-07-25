adding_reasons = True
filename = 'like_prog.txt'
prompt = "Why do you like programming?\n"
prompt += "(enter 'quit' to stop adding reasons)\n"

while adding_reasons:
    reason = input(prompt)
    if reason == "quit":
        adding_reasons = False
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{reason}\n")
