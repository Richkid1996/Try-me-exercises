glossary = {'if statement': 'The simplest kind of if statement has one test and one action',
'Tuples': 'A list of items that cannot be changed',
'Range function': 'Makes it easy to generate numbers',
'key': 'The first item in a key-value pair in a dictionary.', 
'value': 'An item associated with a key in a dictionary.',
'conditional test': 'A comparison between two values.',
'float': 'A numerical value with a decimal component.',
'boolean expression': 'An expression that evaluates to True or False.',}

for term, definition in glossary.items():
	print(f"\n{term.title()}: {definition}")
	