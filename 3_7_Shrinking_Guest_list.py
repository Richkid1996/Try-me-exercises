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


# Dinner table won't arrive on time remove some guest.
print(f"\nSorry I can only invite two guest to my dinner party.")


guest_removed = guest.pop(0)
print(f"\nSorry {guest_removed}, I can't invite you to my dinner")

guest_removed = guest.pop(1)
print(f"\nSorry {guest_removed}, I can't invite you to my dinner")

guest_removed = guest.pop(0)
print(f"\nSorry {guest_removed}, I can't invite you to my dinner")

guest_removed = guest.pop(2)
print(f"\nSorry {guest_removed}, I can't invite you to my dinner")

#The two people who are still invited to my dinner 
names = guest[0].title()
print(f"\nHey {names}, your still invited to my dinner party")

names = guest[1].title()
print(f"\nHey {names}, your still invited to my dinner party")

#Empty the list
del guest[0]
del guest[0]

print(guest)