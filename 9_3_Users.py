class Users:
	"""A class describing users"""
	def __init__(self, first_name, last_name, birthday, code):
		self.first_name = first_name
		self.last_name = last_name
		self.birthday = birthday
		self.code = code 

	def describe_user(self):
		"""Describe the user and print the information"""
		print(f"{self.first_name}, {self.last_name}")
		print(f" Birthday: {self.birthday}")
		print(f" Code: {self.code}")


	def greet_user(self):
		"""Greet the user"""
		print(f"\nHello {self.first_name} {self.last_name} welcome back!!!")


rico = Users('Rico', 'Robinson', '11/14/1996', '345678')
rico.describe_user()
rico.greet_user()

scooter = Users('Scooter', 'Yates', '06/15/1996', '68794848')
scooter.describe_user()
scooter.greet_user()

peewee = Users('Ladarius', 'Green', '03/18/1992', '6784321')
peewee.describe_user()
peewee.greet_user()