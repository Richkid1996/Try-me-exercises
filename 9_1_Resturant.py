class Restaurant:
	"""A simple attempt at a resturant"""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize name and cuisine"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_resturant(self):
		"""Display a summery of the resturant"""
		msg = f"{self.restaurant_name} serves mainly {self.cuisine_type} food."
		print(f"\n{msg}")

	def open_resturant(self):
		"""Give a message that the resturant is now open"""
		msg = f"{self.restaurant_name} is now open for buisness!!!"
		print(f"\n{msg}")


# Now make a instance class for the resturant
restaurant = Restaurant("the mean queen", "pizza")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_resturant()
restaurant.open_resturant()		

