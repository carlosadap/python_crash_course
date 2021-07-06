from random import choice

lottery_numbers = [i for i in range(50)]

winning_numbers = set()

while len(winning_numbers) < 5:
    winning_numbers.add(choice(lottery_numbers))

# print(f"The winning numbers are: {winning_numbers}")

my_numbers = set(range(5))

counter = 0

while winning_numbers != my_numbers:
    winning_numbers = set()
    while len(winning_numbers) < 5:
        winning_numbers.add(choice(lottery_numbers))
    counter += 1

print(f"The winning numbers are: {winning_numbers}")
print(f"It took {counter} iterations to win.")
