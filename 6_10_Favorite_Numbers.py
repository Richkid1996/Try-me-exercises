favorite_numbers = {"Ken":[ 67,68,69,70,24,8], "Rob": [75,76,77,88,99,36], "Kevin": [69,78,45,34,23]}

for name, numbers in favorite_numbers.items():
	print(f"\n{name} likes these numbers")
	for number in numbers:
		print(f"{number}")