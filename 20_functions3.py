#Functions_and_Files

from sys import argv
script, input_file = argv

def print_all(file):
    print(file.read())

#moves to "postion 0," the start of the file
def rewind(file):
    file.seek(0)

def print_a_line(line_count, file):
    print(line_count, file.readline())

current_file = open(input_file)

print("First, let's print the whole file:\n")
print_all(current_file)

print("Be kind, rewind.")
rewind(current_file)

print("Let's print 3 lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
