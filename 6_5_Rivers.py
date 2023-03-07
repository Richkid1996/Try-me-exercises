rivers = {'nile': 'egypt','yellow': 'china', 'mississippi': 'america', 'yangtze': 'china', 'angara': 'russia' }

for  river, country in rivers.items():
	print(f"\nThe {river.title()} runs through {country.title()}.")

print("\nThe following rivers are in this Python code:")
for river in rivers.keys():
	print(f"\n-{river.title()}")

print("\nThe following countries are in this Python code:")
for country in rivers.values():
	print(f"\n-{country.title()}")
