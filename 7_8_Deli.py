sandwich_order = ["Tuna ", "Cheese ", "Turkey ", "Ham "]

finished_sandwhiches = []

while sandwich_order:
	current_orders = sandwich_order.pop()

	print(f"\nI'm still working on your {current_orders} sandwich.")
	finished_sandwhiches.append(current_orders)

print("\n")
for sandwich in finished_sandwhiches:
	print(f"\nI made a {sandwich} sandwich")


