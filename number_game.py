import random

hidden_number = random.randint(1, 100)

#print (hidden_number)
for i in range(10):
    number = int(input("what is you guess?"))
    if number == hidden_number:
        print ("good job! you win!")
    elif number > hidden_number:
        print ("not quite! go lower!")
    elif number < hidden_number:
        print ("not quite! go higher!")
if number != hidden_number:
    print (f"not quite! the number was {hidden_number}")
    