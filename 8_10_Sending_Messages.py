def show_messages(messages):
	"""Print a simple message """
	for message in messages:
		print(message)

def send_messages(messages, sent_messages):
	"""Print each text message and move each message"""
	print("\nSending all messages:")
	while messages:
		current_message = messages.pop()
		print(current_message)
		sent_messages.append(current_message)



messages = ['Hope your having a good day', 'Stay bleesed']
show_messages(messages)


sent_messages = []
send_messages(messages,sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)