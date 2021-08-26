import json

filename = 'fav_number.json'

try:
    with open(filename) as f:
        fav_number = json.load(f)
except FileNotFoundError:
        fav_number = None

if fav_number:
    print(f"Your favorite number is: {fav_number}")
else:
    with open(filename, 'w') as f:
        fav_number = int(input("What's your favorite number? "))
        json.dump(fav_number, f)