#Start off with an empty list 
people = []

#Then create three dictionaries that store three different people and add them to the empty list
person = {'first_name': 'Scooter', 'last_name': 'Yates', 'age': 26, 'City': 'Pensacola'}
people.append(person)

person = {'first_name': 'Rico', 'last_name': 'Robinson', 'age': 26, 'City': 'Pensacola'}
people.append(person)

person = {'first_name': 'Peewee', 'last_name': 'Green', 'age': 33, 'City': 'Pensacola'}
people.append(person)

#Then creat a for loop that prints out the information in the list
for person in people:
	name = f"{person['first_name']} {person['last_name']}"

	age = person['age']

	city = person['City']

	print(f"{name}, of {city}, is {age} years old.")