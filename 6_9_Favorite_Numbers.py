favorite_places = {'Rico': ['florida' ,'las Vegas', 'Cali'], 'Scooter': ['Las Vegas', 'Florida'], 'Peewee': ['Florida']}

for name, places in favorite_places.items():
	print(f"\n{name} likes the following places:")
	for place in places:
		print(f"-{place}")