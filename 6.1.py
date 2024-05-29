countries_capitals = {
    'Russia': 'Moscow',
    'USA': 'Washington',
    'China': 'Beijing',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome'}

# a)
for country, capital in countries_capitals.items():
    print(f'{country}: {capital}')

# b)
country = 'Russia'
print(f'The capital of {country}: {countries_capitals.get(country, "Country not found")}')

# c)
sorted_countries = sorted(countries_capitals.keys())
for country in sorted_countries:
    print(f'{country}: {countries_capitals[country]}')