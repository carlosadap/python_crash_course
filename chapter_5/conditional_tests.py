# Conditional Tests

## 5-1. Conditional Tests:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

## 5-3. Alien Colors #1:

alien_color = "green"

if alien_color == "green":
    print("You earned 5 points!")
else:
    print("You earned 10 points!")

alien_color = "red"

if alien_color == "green":
    print("You earned 5 points!")
else:
    print("You earned 10 points!")

## 5-5. Alien Colors #3:

alien_color = "green"

if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
elif alien_color == "red":
    print("You earned 15 points!")

alien_color = "yellow"

if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
elif alien_color == "red":
    print("You earned 15 points!")

alien_color = "red"

if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
elif alien_color == "red":
    print("You earned 15 points!")

## 5-6. Stages of Life:

person_age = 5

if person_age < 2:
    print("The person is a baby")
elif person_age < 4:
    print("The person is a toddler")
elif person_age < 13:
    print("The person is a kid")
elif person_age < 20:
    print("The person is a teenager")
elif person_age < 65:
    print("The person is an adult")
elif person_age >= 65:
    print("The person is a elder")

# #5-8. Hello Admin:

usernames = ["admin", "user_0", "user_1", "user_2", "user_3"]
# usernames = []

if usernames:
    for user in usernames:
        if user == "admin":
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")

## 5-10. Checking Usernames:

print("\n")
current_users = ["admin", "usEr_0", "user_1", "user_2", "user_3"]
new_users = ["admiN", "user_4", "user_5", "user_6", "user_0"]

for new_user in new_users:
    lower_current_users = [user.lower() for user in current_users]
    if new_user.lower() in lower_current_users:
        print(f"{new_user} is already being used, you should pick another username")
    else:
        print(f"{new_user} username is available")

## 5-11. Ordinal Numbers:

print("\n")

ordinal_list = range(1,10)
print(ordinal_list)