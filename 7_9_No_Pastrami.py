sandwich_order = ["Tuna ","Pastrami", "Cheese ","Pastrami", "Turkey ", "Ham ","Pastrami"]

finished_sandwhiches = []
#Print a message that we are all out of Pastrami
print("We are all out of Pastrami")

while "Pastrami" in sandwich_order:
	sandwich_order.remove("Pastrami")

while sandwich_order:
	current_orders = sandwich_order.pop()

	print(f"\nI'm still working on your {current_orders} sandwich.")
	finished_sandwhiches.append(current_orders)

print("\n")
for sandwich in finished_sandwhiches:
	print(f"\nI made a {sandwich} sandwich")

