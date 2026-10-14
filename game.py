import random
word_list = ["clear your desk","make your bed"," open windows","clear a section of floor"]
hidden_word = random.choice(word_list)
print (" hey girl.... ik you dont want to clean...")
print (" SOOOOOOOOOOOOOOOOO")
print ("drum roll please.....")
import time
time.sleep(4)
print (" WELCOME TO MY CLEANING GAME!!!!")
print (" pretty much, every question you get wrong, you have to clean some thing!")
import time
time.sleep(2)
answer = input(" ready to play?")
if answer == "yes":
    print ("ok!")
else:
    print (f"already got one wrong... you gotta {hidden_word}")
dog = input("lady gagas birth name?")
if answer == "Stefani":
    print ("good job!")
else:
    print (f"shucks, nope! you gotta {hidden_word} ")
