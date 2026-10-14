import random 
import time

word_list = [ "clear your desk", "make your bed", "open windows", "clear a section of floor" ]

print("hey girl.... ik you dont want to clean...") 
print("SOOOOOOOOOOOOOOOOO") 
print("drum roll please.....") 
time.sleep(4)

print("WELCOME TO MY CLEANING GAME!!!!") 
print("pretty much, every question you get wrong, you have to clean something!") time.sleep(2)

answer = input("ready to play? ").lower()

if answer in ["yes", "yeah"]: print("ok!")

elif answer in ["no", "nah", "nope"]: print("already got one wrong...")

else: print("girl, that's not an answer 😭")

def cleaningtask(): 
    if len(wordlist) > 0: hiddenword = random.choice(wordlist) wordlist.remove(hiddenword) print(f"you gotta {hidden_word}!") else: print("GIRL YOU'VE DONE ALL THE CLEANING TASKS!! 🎉")



if answer in ["no", "nah", "nope"]: cleaning_task()