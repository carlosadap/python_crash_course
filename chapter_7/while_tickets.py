# 7-5. 

prompt = "\nWhat is your age?"
prompt += "\n(Enter '0' to stop asking the age) "

asking = True

while asking:
    age = input(prompt)
    age = int(age)

    if age == 0:
        asking = False
    elif age < 3:
        print("Under the age of 3, tickets are free")
    elif age <= 12:
        print("Between the ages of 3 and 12, the ticket is $10")
    else:
        print("Above 12, the ticket is $15")

