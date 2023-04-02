def city_country(city, country):
	"""Return a string like 'Santiago, Chile'"""
	return f"{city.title()}, {country.title()} "

city = city_country('pensacola', 'america')
print(city)

city = city_country('Miami', 'america')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)