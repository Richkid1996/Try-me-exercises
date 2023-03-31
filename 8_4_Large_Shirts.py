def make_shirt(size='Large', text='I love Python'):
	"""Display the size of the shirt and the message printed on it."""
	print(f"\nThe shirt size is {size}.")
	print(f"Has the saying {text} printed on the back.")

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Your crazy.')