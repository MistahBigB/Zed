#33 While Loops
import random

i = 0
numbers = []

while i < 10001:
    print(f"At the top i is {i}.")
    numbers.append(i)

    i +=random.choice(list(range(1, 101)))
    print("Numbers now: ", numbers)
    print(f"At the bottom of i is {i}.")

'''
def lupe(max):
    i=0
    numbers = []
    inc = 5
    while i < max:
        print(f"At the top i is {i}.")
        numbers.append(i)

        i += inc
        print("Numbers now: ", numbers)
        print(f"At the bottom of i is {i}.")

        if (i > 500):
            print("Sayonara")
            break

    print("The numbers: ")

    for num in numbers:
        print(num)


The limit for this function call is the nested if in the lupe function
lupe(5001)
'''


'''
Completing the task with a for loop
numbers = []

for i in range(1, 10):
    print(f"At the top of i is {i}.")
    numbers.append(i)

    i +=1
    print("Numbers now: ", numbers)
    print(f"At the bottom of i is {i}.")
'''
