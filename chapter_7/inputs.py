#7-1. Rental car

car = input("\nWhat kind of rental car would you like? ")

print(f"\nLet me see if I can find a {car.title()}")

# 7-2. Restaurant Seating:

num_people = input("\nHow many people are in your dinner group? ")
num_people = int(num_people)

if num_people > 8:
    print("\nYou will have to wait for a table.")
else:
    print("\nYour table is ready.")


# 7-3. Multiples of Ten:

number = input("\nEnter a number, and I'll tell you if it's divible by ten or not: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is divisible by ten")
else:
    print(f"\nThe number {number} is not divisible by ten")