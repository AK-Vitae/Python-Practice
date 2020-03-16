cities = {
    'New York City': {
        'country': 'usa',
        'population': 8_623_000,
        'fact': 'New York City is made up of five boroughs: Manhattan, The Bronx, Queens, Brooklyn, and Staten Island'
    },
    'Tokyo': {
        'country': 'japan',
        'population': 9_273_000,
        'fact': 'Vending machines are available in Tokyo at every 12 meter distance'
    },
    'Mumbai': {
        'country': 'india',
        'population': 18_410_000,
        'fact': 'There is only 1.1 square metres of open space for people living in Mumbai'
    }
}
for city, city_info in cities.items():
    print(f'{city}:')
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    if city_info['country'] == 'usa':
        print(f'\tCountry: {country.upper()}')
    else:
        print(f'\tCountry: {country.title()}')
    print(f'\tPopulation: {population}')
    print(f'\tInteresting fact: {fact}.')
    print('\n')
