#38 Lists
import random

ten_things = "Doom Skating Gummies Brothers Girlfriend Travel Lifting Rest"
#ten_things_str = str(ten_things)

#print(ten_things_str)
print("It's important to count your blessings. Here are 10 things that I like:")
stuff = ten_things.split(' ')
print(f"{stuff}")
print(f"There are only {len(stuff)} things in that list. Let's fix that.")

while len(stuff) != 10:
    more_stuff = input("What's something that you like?\n>")
    print("Adding: ", more_stuff)
    stuff.append(more_stuff)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)
print("Let's do some things with this list.")

#In order to properly sort alphabetically, all entries must be similarly formatted
#e.g. they must all be in all caps, or have the first letter capitalized, etc
favorite = random.choice(stuff)
print(f"My favorite of all of these is {favorite}")
stuff.sort()
print("Sorted alphabetically: ", stuff)
stuff.reverse()
print("Reverse alphabetically: ", stuff)
print(stuff[1]) #prints position 1, the second item in the list
print(stuff[-1]) #prints the last item in the list
print(stuff.pop()) #pops off the last item in the list
print(' '.join(stuff)) #joins the items in the list 'stuff'
print('#'.join(stuff[3:5])) #extracts a slice from the stuff list from position 3 to position 4, like range(3,5) does not include 5
