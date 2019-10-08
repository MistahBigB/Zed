#opening2.py
#opening again, but with just user inputs, not argvs

filename = input("What file would you like to open?\n> ")
print(f"Opening {filename}")
txt = open(filename)
#only reads the first line of the file
print(txt.readline())
#only reads the 2nd line
print(txt.readline())
txt.close()
