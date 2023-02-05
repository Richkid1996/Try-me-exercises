places = ["Italy", "Brazil", "Austrilla", "Dubi", "Jamacia"]

# putting the list in alphabetical order using the sorted method()
print(f"\nUsing Sorted() to put the list in alphabetical order")
print(sorted(places))

print(f"\nUsing Sorted() to put the list in reverse order ")
print(sorted(places, reverse=True))

# Using the reverse method
print(f"\nUsing Reverse to change the order of the list")
places.reverse()
print(places)

print(f"\nUsing Reverse to change the order of the list again")
places.reverse()
print(places)

# still in original order 
print(f"\nThis is the original order")
print(places)

# Using the sort method()
print(f"\nUsing the sort method to change the list to alphabetical order permanently")
places.sort()
print(places)

print(f"\nUsing the sort method to reverse the list so it's sorted in reverse alphabetical order")
places.sort(reverse=True)
print(places)