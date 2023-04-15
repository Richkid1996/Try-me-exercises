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


# Now make 3 instances class for the resturant
the_mean_queen = Restaurant("the mean queen", "pizza")
the_mean_queen.describe_resturant()

	

the_zone = Restaurant("the zone", "wings")
the_zone.describe_resturant()


the_blue_dog = Restaurant("the blue dog", "seafood")
the_blue_dog.describe_resturant()
