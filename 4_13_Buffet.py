#This is how you write a tuple which is a list that can't be modified just updated
buffet = ('pizza', 'corndogs', 'hotdogs', 'fries', 'burgers')

print("\nOrignal food menu:")
for food in buffet:
	print(food)

# This just shows that you will get an error if you try to modify the tuple 
#buffet.append('fish sticks')

print("\nModified food menu:")
buffet = ('pizza', 'corndogs', 'hotdogs', 'fish sticks', 'ice cream')
for food in buffet:
	print(food)