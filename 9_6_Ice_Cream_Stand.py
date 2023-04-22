class Restaurant:
	"""A simple attempt at a resturant"""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize name and cuisine"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_resturant(self):
		"""Display a summery of the resturant"""
		msg = f"{self.restaurant_name} serves mainly {self.cuisine_type} food."
		print(f"\n{msg}")

	def open_resturant(self):
		"""Give a message that the resturant is now open"""
		msg = f"{self.restaurant_name} is now open for buisness!!!"
		print(f"\n{msg}")

	def set_number_served(self, number_served):
		"""Allow user to set the number of customers served."""
		self.number_served = number_served

	def increment_number_served(self, additional_served):
		"""Increment the number of customers who've all ready been served"""
		self.number_served += additional_served

class IceCreamStand(Restaurant):
	"""Represents a specific restaurant"""
	def __init__(self, restaurant_name, cuisine_type='ice_cream'):
		"""Initialize attributes of the parent class."""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []


	def show_flavors(self):
		"""Show ice cream flavors"""
		print("\nThses are the following flavors available:")
		for flavor in self.flavors:
			print(f"- {flavor}")

		

big_one = IceCreamStand('The Big one')
big_one.flavors = ['strawberry', 'cheesecake', 'Banana pudding']
big_one.show_flavors()