prompt = "\nplease enter your burger toppins here: "
prompt += "\nEnter 'quit' when your done. "


while True:
	topping = input(prompt)

	if topping != 'quit':
		print(f"\nI'll add {topping}, to your pizza")
	else:
		break