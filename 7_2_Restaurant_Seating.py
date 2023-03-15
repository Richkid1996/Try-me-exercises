#have to assign it to a variable to change it to numerical reading
seating = input("How many people are in your dinner group ")
seating = int(seating)

if seating > 8:
	print("You will  have to wait on a table")
else:
	print("Your table is ready")