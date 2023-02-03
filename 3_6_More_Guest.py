# Invite some people to dinner 
guest = ["Crag", "Scooter", "Peewee"]

names = guest[0].title()
print(f"{names}, please come to dinner.")

names = guest[1].title()
print(f"{names}, please come to dinner.")

names = guest[2].title()
print(f"{names}, please come to dinner.")

names = guest[0].title()
print(f"\n{names}, can't make it to the dinner.")

guest[0] = 'Robert'

print(guest)

names = guest[0].title()
print(f"\n{names}, please come to dinner.")

names = guest[1].title()
print(f"{names}, please come to dinner.")

names = guest[2].title()
print(f"{names}, please come to dinner.")


print(f"\nI've found a bigger dinner table\t")

#Using inser() to add a guest at the beginning of the list.
guest.insert(0, "Ray")
#using insert to add a guest at the middle of the list. 
guest.insert(1, "Rob")
#Using append to add one new guest to the end of the list.
guest.append("Ken")

names = guest[0].title()
print(f"\n{names}, please come to dinner.")

names = guest[1].title()
print(f"\n{names}, please come to dinner.")

names = guest[2].title()
print(f"\n{names}, please come to dinner.")

names = guest[3].title()
print(f"\n{names}, please come to dinner.")

names = guest[4].title()
print(f"\n{names}, please come to dinner.")

names = guest[5].title()
print(f"\n{names}, please come to dinner.")
