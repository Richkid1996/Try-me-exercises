my_foods = ['pizza', 'falafel', 'carrot cake']

# This is how you copy a list 
friends_food = my_foods[:]

#This is how you add to two different list
my_foods.append('pasta')
friends_food.append('BBQ')

print("\nMy favorite foods are:")
for food in my_foods:
	print(food)

print("\nMy friends favorite foods are:")
for friend in friends_food:
	print(friend)