#18_functions
#takes all the args listed in the function and put them in a list
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("Nada, y tu?")

print_two("Baconius", "Maximus")
print_two_again("Baconioso", "Maximoso")
print_one("Bacon!")
print_none()
