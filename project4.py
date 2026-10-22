import random
import time

hidden_number = random.randint(1, 100)


#line 8 is for testing
#print (hidden_number)
print("welcome to my guessing game!")
time.sleep(1)
print ("select your difficulty-")

print ("A-- easy")
print ("B-- normal")
print ("C-- hard")
level = input("D-- EXTREME")
if level == "A" or level == "a" or level == " a" or level == "A " or level == " A" or level == " a ":
    print ("you have 100 guesses to guess a number between 1 and 100.")
    time.sleep(1)
    for i in range(100):
    
    # loop starts here!
        number = int(input("what is you guess?"))
            
        if number == hidden_number and i == 0:
            print (f"good job! the number was {hidden_number} and you won on your first try!")
        elif number == hidden_number and i == 5:
            print (f"good job! the number was {hidden_number} and you won on your last try!")
            quit()
        elif number == hidden_number and i != 0:
            print (f"good job! the number was {hidden_number} you win!")
            quit()
        elif number > hidden_number:
            print (f"not quite! {number} is too high, go lower")
        elif number < hidden_number:
            print (f"not quite! {number} is too low, go higher")
        elif number != hidden_number and i == 100:
        #loop ends here
            print (f"not quite! the number was {hidden_number}")
            quit()
        else:
            print ("please pick a number between 1-100!")
            quit()
elif level == "B" or level == "b" or level == " b" or level == "B " or level == " B" or level == " b ":
    print ("you have 10 guesses to guess a number between 1 and 100.")
    time.sleep(1)
    for i in range(10):
        
        # loop starts here!
            number = int(input("what is you guess?"))
            time.sleep(1)
                
            if number == hidden_number and i == 0:
                print (f"good job! the number was {hidden_number} and you won on your first try!")
            elif number == hidden_number and i == 10:
                print (f"good job! the number was {hidden_number} and you won on your last try!")
                quit()
                quit()
            elif number == hidden_number and i != 0:
                print (f"good job! the number was {hidden_number} you win!")
                quit()
            elif number > hidden_number:
                print (f"not quite! {number} is too high, go lower")
            elif number < hidden_number:
                print (f"not quite! {number} is too low, go higher")
            elif number != hidden_number and i == 10:
            #loop ends here
                print (f"not quite! the number was {hidden_number}")
                quit()
            else:
                        print ("please pick a number between 1-100!")
                        quit()
elif level == "C" or level == "c" or level == " c" or level == "C " or level == " C" or level == " c ":
    print ("you have 5 guesses to guess a number between 1 and 100.")
    for i in range(5):
            
            # loop starts here!
                number = int(input("what is you guess?"))
                time.sleep(1)
                    
                if number == hidden_number and i == 0:
                    print (f"good job! the number was {hidden_number} and you won on your first try!")
                    quit()
                elif number == hidden_number and i == 5:
                                    print (f"good job! the number was {hidden_number} and you won on your last try!")
                                    quit()
                elif number == hidden_number and i != 0:
                    print (f"good job! the number was {hidden_number} you win!")
                    quit()
                elif number > hidden_number:
                    print (f"not quite! {number} is too high, go lower")
                elif number < hidden_number:
                    print (f"not quite! {number} is too low, go higher")
                if number != hidden_number and i == 5:
                #loop ends here
                    print (f"not quite! the number was {hidden_number}")
                    quit()
                else:
                    print ("please pick a number between 1-100!")
                    quit()
elif level == "D" or level == "d" or level == " d" or level == "D " or level == " D" or level == " D ":
    print ("you have 1 guess to guess a number between 1 and 100... lock in")
    time.sleep(1)
    print("...") 
    time.sleep(1)
     
    
 #print hidden number                
                 # no loop this time!
    number = int(input("what is you guess? remember, gotta get this right..."))
    time.sleep(1)
    
    if number == hidden_number:
        print (f"good job! the number was {hidden_number} and you won on your first (and only) try!")
        quit()
    elif number != hidden_number:
        print (f"not quite! the number was {hidden_number}, guess you shouldnt have chosen extreme...A")
        quit()

