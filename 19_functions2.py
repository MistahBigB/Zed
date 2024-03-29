#19_functions2

def cheese_and_crackers(cheese_count, boxes_of_crackers):
        print(f"You have {cheese_count} cheeses!")
        print(f"You have {boxes_of_crackers} boxes of crackers!")
        print("Don't bring them to bed!")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 6 * 9)

print("And we can combine the two, variables AND math:")
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers + 1000)

print("Finally, we can just ask!")  #user input is automatically a string
amount_of_cheese = input("How much cheese do you have?")
amount_of_cheese = int(amount_of_cheese)
amount_of_crackers = input("How many crackers do you have?")
amount_of_crackers = int(amount_of_crackers)

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
