def make_shirt(size, text):
	"""Display the size of the shirt and the message printed on it."""
	print(f"\nThe shirt size is {size}.")
	print(f"Has the saying {text} printed on the back.")

make_shirt('X-Large', '"We doing Numbers!"')
make_shirt(size='XL', text='"We doing Numbers!"')