car = "bmw"
# Checking for Equality
print("\n Is car == 'bmw'? I predict True.")
print(car == 'bmw')

print("\n Is car == 'audi'? I predict False.")
print(car == 'audi')

car = 'bently'
print("\n Is car == 'bently'? I predict True.")
print(car == 'bently')

print("\n Is car == 'rolls royce'? I predict False.")
print(car == 'rolls royce')

# Testing using the lower() method 
car = 'Bently'
print("\n Is car == 'Bently'? I predict False.")
print(car == 'Bently')

print("\n Is car == 'Bently'? I predict True.")
print(car.lower() == 'bently')

# Checking for Inequality !=
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("\nHold the anchovies!")


# Numerical test
age = 18
print("\n Is age is == 18? I predict True")
print(age == 18)

age = 18
if age != 16:
	print("\nRequired age is 18!")

age_0 = 22
age_1 = 18
print("\n Is age_0 >= 21 or age_1 >= 21? I predict True.")
print(age_0 >= 21 or age_1 >= 21)


# Testing if a value is whithin a list 
requested_topping = ["mushrooms", "onions", "pineapple"]
print("\nIs mushrooms in requested_topping list? I predict True.")
print('mushrooms' in requested_topping)

print("\nIs peperoni in requested_topping list? I predict False.")
print('peperoni' in requested_topping)