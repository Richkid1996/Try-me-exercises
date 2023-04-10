def make_sandwiches(*toppings):
	"""Collect as many toppings as the function call provides and print the summary"""
	print("\nMaking a sandwich with the following toppings:")
	for topping in toppings:
		print(f"\n-adding {topping} to your sandwich.")
		print("Your sandwich is ready!!!")


make_sandwiches("turkey")
make_sandwiches("Cheese", "Ham", "Lettuce")
make_sandwiches("Chicken", "Bacon", "Mayo")