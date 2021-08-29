def get_formatted_city(city, country, population=''):
    """Generate a neatly formated City, Country"""
    if population:
        formated_city = f"{city}, {country}"
        formated_city = formated_city.title()
        formated_city += f" - population {population}"
    else:
        formated_city = f"{city}, {country}"
        formated_city = formated_city.title()
    
    return formated_city
