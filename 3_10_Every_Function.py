countries = ["Italy", "Brazil", "Austrilla", "Dubi", "Jamacia"]

#append() method to add China to the end of the list
print(f"\nUsing the append() method to add an element to the list")
countries.append('China')
print(countries)

#insert() method to insert russia at the 3 spot
print(f"\nUsing the insert()")
countries.insert(2, "Russia")
print(countries)

# using the del statment to remove russia 
print(f"\nUsing the del statment")
del countries[2]
print(countries)

#Using the pop() method to remove china
print(f"\nUsing the pop()")
remove_contry = countries.pop()
print(countries)


# putting the list in alphabetical order using the sorted method()
print(f"\nUsing Sorted() to put the list in alphabetical order")
print(sorted(countries))

print(f"\nUsing Sorted() to put the list in reverse order ")
print(sorted(countries, reverse=True))

# Using the reverse method
print(f"\nUsing Reverse to change the order of the list")
countries.reverse()
print(countries)

print(f"\nUsing Reverse to change the order of the list again")
countries.reverse()
print(countries)

# still in original order 
print(f"\nThis is the original order")
print(countries)

# Using the sort method()
print(f"\nUsing the sort method to change the list to alphabetical order permanently")
countries.sort()
print(countries)

print(f"\nUsing the sort method to reverse the list so it's sorted in reverse alphabetical order")
countries.sort(reverse=True)
print(countries)

# we use len() to tell us how many places are within the list
number_of_places = len(countries)
print(f"\nWe plan on going to {number_of_places} different countries ")