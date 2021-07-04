def display_message():
    print("\nI am learning about functions!")


display_message()


def favorite_book(title):
    print(f"\nOne of my favorite books is {title}")


favorite_book("The Solitaire Mystery")


def make_shirt(size, text):
    print(
        f"The shirt will be of size {size} and will have the following message: {text}")


make_shirt("M", "It's time to get schwifty")


def make_shirt(text, size="L"):
    print(
        f"The shirt will be of size {size} and will have the following message: {text}")


make_shirt("It's time to get schwifty")


def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}")


describe_city("Madrid", "Spain")
describe_city("Paris", "France")
describe_city("Reykjavik")


def city_country(city, country):
    return f"\n{city.title()}, {country.title()}"


city_0 = city_country("Madrid", "spain")
print(city_0)
city_1 = city_country("paris", "FrAnCe")
print(city_1)
city_2 = city_country("bERLIN", "GermanY")
print(city_2)


def make_album(artist, title, num_songs=None):
    return {"artist": artist, "title": title, "number of songs": num_songs}


album_1 = make_album("Pink Floyd", "The Dark Side of the Moon", 10)
album_2 = make_album("Beatles", "The White Album")
album_3 = make_album("Nação Zumbi", "Da Lama ao Caos")

print(album_1)
print(album_2)
print(album_3)

making_albums = True
while making_albums:
    print("\nPress 'q' to stop making albums")
    artist = input("Enter the name of the band ")
    if artist == 'q':
        break
    title = input("Enter the name of the title of the album ")
    if title == 'q':
        break
    num_songs = input("Enter the number of songs ")
    if num_songs == 'q':
        break

    album = make_album(artist, title, num_songs)
    print(album)


def make_sandwich(*items):
    print("\nYour sandwich is going to have:")

    for item in items:
        print(f"- {item}")


make_sandwich("cheese")
make_sandwich("cheese", "ham", "meat")
make_sandwich("cheese", "ham", "meat", "eggs", "sauce")

def build_profile(first, last, **kwargs):
    kwargs['first_name'] = first
    kwargs['last_name'] = last
    return kwargs

my_profile = build_profile('carlos', 'albu', planet='Earth', field='Promistry')

print(my_profile)

def build_car(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

my_car = build_car('subaru', 'outback', color='blue', towpackage=True)
print(my_car)


