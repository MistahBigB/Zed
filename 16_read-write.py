#read-write.py
from sys import argv

script, filename = argv

txt = open(filename)
print(txt.read())
print("\n")

print(f"We're going to erase {filename}.")
print("To escape, press CTRL-C.")
print("To continue, press ENTER.")
input("?")

print("Opening the file...")
target = open(filename, 'w+')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for a line. Pick a song, or a poem!")

#Can this be done with a for loop?
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("\n")
print("I'll write those lines to the file.")

target.write(line1+"\n"+line2+"\n"+line3+"\n")
# target.write(line2, "\n")
# target.write(line3, "\n")
target.close()

print("All done! Check it out!")
txt = open(filename)
print(txt.read())


print("Closing the file.")
target.close()
