prompt1 = "\nEnter a numerical input to sum: "
prompt2 = "\nEnter another numerical input: "
adding_nums = True

def tell_quit(str):
    str += "\n(Enter 'q' to quit) "
    return str

def check_break(q):
    if q == "q":
        return True

while adding_nums:
    num1 = input(tell_quit(prompt1))
    if check_break(num1):
        break

    num2 = input(tell_quit(prompt2))
    if check_break(num2):
        break
    
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print(f"Sorry, {num1} or {num2} is not a number")
        print("-----------------------")
    else:
        print(f"{num1} + {num2} is equal to {num1 + num2}")
        print("-----------------------")
