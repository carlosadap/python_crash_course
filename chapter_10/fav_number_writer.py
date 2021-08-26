import json

filename = 'fav_number.json'

with open(filename, 'w') as f:
    fav_number = int(input("What's your favorite number? "))
    json.dump(fav_number, f)