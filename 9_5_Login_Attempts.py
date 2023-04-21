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






rico = Users('Rico', 'Robinson', '11/14/1996', '345678')
rico.describe_user()
rico.greet_user()

print("\nMaking 3 login attempts...")
rico.increment_login_attempts()
rico.increment_login_attempts()
rico.increment_login_attempts()
rico.increment_login_attempts()
print(f"\nLogin attempts: {rico.login_attempts}")

print("\nReseting login attempts...")
rico.reset_login_attempts()
print(F" Login attempts: {rico.login_attempts}")