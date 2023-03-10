#Create an empty list to store the dictionaries in
pets = []

#Create a few dictionaries describing peoples picks 

animal = {'animal_type': 'Dog', 'pet_name': 'jojo', 'owners_name': 'Jim'}
pets.append(animal)

animal = {'animal_type': 'Cat', 'pet_name': 'poppy', 'owners_name': 'Sarah'}
pets.append(animal)

animal = {'animal_type': 'Fish', 'pet_name': 'junebug', 'owners_name': 'Larry'}
pets.append(animal)

for animal in pets:
	print(f"This is what I know about {animal['pet_name']}")
	for key, value in animal.items():
		print(f"\t{key}: {value}")
