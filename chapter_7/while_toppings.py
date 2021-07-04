# 7-4. Pizza Toppings:

toppings = []
adding = True

prompt = "\nWhich topping would you like to add?"
prompt += "\n(Enter quit to stop adding toppings) "

while adding:
    topping = input(prompt)

    if topping != "quit":
        toppings.append(topping)
        print(f"{topping} is going to be added to your pizza!")
    else:
        adding = False

print(f"\nYour toppings are: {toppings}")

