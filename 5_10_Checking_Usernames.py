current_users = ['rico', 'james', 'rob','ray', 'ken', 'kevin']
new_users = ['black', 'james', 'peewee', 'crag', 'ken']

#This is for case sensitivity
current_users_lower = [user.lower() for user in current_users]


for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print(f"\n{new_user}, is already being used select new user name.")
	else:
		print(f"\nThis username {new_user} is available")