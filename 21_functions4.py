#21 Functions can return something

def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def sub(a, b):
    print(f"Subtracting {b} from {a}")
    return b - a

def mult(a, b):
    print(f"Multiplying {a} by {b}")
    return a * b

def div(a, b):
    print(f"Dividing {a} by {b}")
    return a / b

print("Maaaaaaaaaaaaaaaaaaaaaaaaaath!!!!!")

age = add(30, 4)
height = sub(2, 72)
weight = mult(45, 4)
iq = div(10000, 80)

print(f"Age: {age},\nHeight: {height},\nWeight: {weight},\nIQ: {iq}\n")

print("Here is a puzzle")
what = add(age, sub(height, mult(weight, div(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
