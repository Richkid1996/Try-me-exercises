class Users:
	"""A class describing users"""
	def __init__(self, first_name, last_name, birthday, code):
		self.first_name = first_name
		self.last_name = last_name
		self.birthday = birthday
		self.code = code
		self.login_attempts = 0 

	def describe_user(self):
		"""Describe the user and print the information"""
		print(f"{self.first_name}, {self.last_name}")
		print(f" Birthday: {self.birthday}")
		print(f" Code: {self.code}")


	def greet_user(self):
		"""Greet the user"""
		print(f"\nHello {self.first_name} {self.last_name} welcome back!!!")

	def increment_login_attempts(self):
		"""Increment the value of login_attempts"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset login attempts"""
		self.login_attempts = 0

class Admin(Users):
	"""This is for a special kind of user"""
	def __init__(self, first_name, last_name, birthday, code):
		"""Initialize attributes of the parent class."""
		super().__init__(first_name, last_name, birthday, code)
		self.privileges = []


	def show_privileges(self):
		"""Display the Admin privileges"""
		print("\nThese are the Admin Privileges:")
		for privilege in self.privileges:
			print(f"- {privilege}")




rico = Admin('Rico', 'Robinosn','11/14/1996', '345678')
rico.describe_user()
rico.privileges = ["can add post", "can delete post", "can ban user"]
rico.show_privileges()