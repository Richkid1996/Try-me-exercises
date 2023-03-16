#Ask the user for a number
number = input("Can you give me a number please: ")
number = int(number)


if number % 10 == 0:
	print(f"{number} is a multiple of ten")
else:
	print(f"{number} isn't a multiple of ten")