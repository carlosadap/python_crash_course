known_person = {
    'first_name': "John",
    'last_name': "Doe",
    'age': 33,
    'city': "Foo"
}

print(known_person)
print()

fav_numbers = {
    'p_1': 1,
    'p_2': 2,
    'p_3': 3,
    'p_4': 4,
    'p_5': 5,
    'p_6': 6,
}

print(fav_numbers)
print()

known_person_0 = {
    'first_name': "Jon",
    'last_name': "Doe",
    'age': 30,
    'city': "Foo"
}

known_person_1 = {
    'first_name': "Joh",
    'last_name': "Doe",
    'age': 31,
    'city': "Bar"
}

known_person_2 = {
    'first_name': "Ohn",
    'last_name': "Doe",
    'age': 32,
    'city': "Spam"
}

people = [known_person_0, known_person_1, known_person_2]

for person in people:
    print(person)


fav_numbers = {
    'p_1': [1,2],
    'p_2': [2,3,4],
    'p_3': [3,4,6,8],
    'p_4': [1,2,8,4],
    'p_5': [5],
    'p_6': [6,4,2],
}

for person, fav_nums in fav_numbers.items():
    print(f"{person}'s favorite numbers are: {fav_nums}")

cities = {
    "Paris": {
        "country":"France",
        "population": 2_175_601,
        "fact": "Since the 17th century, Paris has been one of Europe's major centres of finance, diplomacy, commerce, fashion, gastronomy, science and arts."
    },
    "Berlin": {
        "country": "Germany",
        "population": 3_800_000,
        "fact": "Berlin's urban area, which has a population of around 4.5 million, is the second most populous urban area in Germany after the Ruhr."
    },
    "Madrid": {
        "country": "Spain",
        "population": 3_400_000,
        "fact": "Madrid lies on the River Manzanares in the center of both the country and the Community of Madrid region, of which it is also the capital. As the capital city of Spain, seat of government, residence of the Spanish monarch, Madrid is also the political, economic and cultural centre of the country."
    },

}

for city, info in cities.items():
    print(f"\nThe city of {city} is in {info['country']}, with a population of"
    f" {info['population']}. One interesting fact is that {info['fact']}")
