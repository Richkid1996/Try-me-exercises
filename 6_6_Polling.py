favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name, langauge in favorite_languages.items():
    print(f"{name.title()}'s favorite langauge is {langauge.title()}.")



should_poll = ['jen', 'rico', 'rob', 'kevin', 'ray', 'phil']

for poll in should_poll:
    if poll in favorite_languages:
        print(f"\nThank you for taking the poll {poll.title()}.")

    else:
        print(f"\n{poll.title()}, what is your favorite langauge?")