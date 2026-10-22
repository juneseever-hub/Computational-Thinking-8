print ("hey! welcome to what drink are you quiz! hope you enjoy!!!")
print ("                                  PRESS ENTER TO BEGIN")
input ()
water_points = 0
coke_points = 0
sprite_points = 0 
tea_points = 0 
coffee_points = 0
rootbeer_points = 0
print ("you are lost in the middle of the city... how are you getting home? ")
print ("A: text a friend to pick you up")
print ("B: call a uber to pick up")
print ("C: a bus")
print ("D: lime scooter or bike")
print ("E: walk until you find your house, you need your steps")
print ("F: give up and take a nap")
answer1= input ()
if answer1 == "A":
    coke_points += 1
elif answer1 == "B":
     sprite_points += 1
elif answer1 == "C":
     rootbeer_points += 1
elif answer1 == "D":
     tea_points += 1
elif answer1 == "E":
     water_points += 1
elif answer1 == "F":
     coffee_points += 1
print ("favorite color?")
print ("A: red")
print ("B: orange")
print ("C: yellow")
print ("D: green")
print ("E: blue")
print ("F: purple")
answer2= input ()
if answer2 == "A":
    coke_points += 1
elif answer2 == "D":
     sprite_points += 1
elif answer2 == "F":
     rootbeer_points += 1
elif answer2 == "B":
     tea_points += 1
elif answer2 == "E":
     water_points += 1
elif answer2 == "C":
     coffee_points += 1
print ("free day! where are you going?!")
print ("A: beach")
print ("B: cozy day at home")
print ("C: explore the city")
print ("D: hike")
print ("E: visit friends and family")
print ("F: nothing... i dont have days off...")
answer3= input ()
if answer3 == "C":
    coke_points += 1
elif answer3 == "A":
     sprite_points += 1
elif answer3 == "E":
     rootbeer_points += 1
elif answer3 == "B":
     tea_points += 1
elif answer3 == "D":
     water_points += 1
elif answer3 == "F":
     coffee_points += 1
print ("morning bird? or night owl? maybe you are an afternoon albatross?")
print ("A: morning bird")
print ("B: afternoon albatross")
print ("C: night owl")
answer4= input ()
if answer4 == "C":
    coke_points += 1
elif answer4 == "B":
     sprite_points += 1
elif answer4 == "B":
     rootbeer_points += 1
elif answer4 == "A":
     tea_points += 1
elif answer4 == "C":
     water_points += 1
elif answer4 == "A":
     coffee_points += 1
print ("superpower? ")
print ("A: FLYING!")
print ("B: telepathy")
print ("C: super speed!")
print ("D: talk to animals!")
print ("E: breath under water")
print ("F: invisibility")
answer5= input ()
if answer5 == "A" or answer5 == "a":
    coke_points += 1
elif answer5 == "B":
     sprite_points += 1
elif answer5 == "C":
     rootbeer_points += 1
elif answer5 == "D":
     tea_points += 1
elif answer5 == "E":
     water_points += 1
elif answer5 == "F":
     coffee_points += 1
print ("KAREOKE!!!! what are you singing!!! ")
print ("A: Bad Romance - Lady Gaga")
print ("B: Love Story - Taylor Swift")
print ("C: Grenade - Bruno Mars")
print ("D: Baby - Justin Beiber")
print ("E: I dont sing...")
print ("F: Free Style!!!!!!")
answer6= input ()
if answer6 == "D":
    coke_points += 1
elif answer6 == "B":
     sprite_points += 1
elif answer6 == "C":
     rootbeer_points += 1
elif answer6 == "F":
     tea_points += 1
elif answer6 == "A":
     water_points += 1
elif answer6 == "E":
     coffee_points += 1
print ("thank you for taking my quiz! hit enter to see your results!")
input ()
#this happens when they get the coke ending
if coke_points > sprite_points and coke_points > rootbeer_points and coke_points > tea_points and coke_points > water_points and coke_points > coffee_points:
     print ("You are a nice diet coke! A fun soda that loves to socialize,")
     print ("but sometimes needs to reset on your own! <3")
#this happens when they get the sprite ending
elif sprite_points > coke_points and sprite_points > rootbeer_points and sprite_points > tea_points and sprite_points > water_points and sprite_points > coffee_points:
     print ("You are a sprite person! nobody loves you, nobody hates you...")
     print ("youll do for now")
     #this happens when they get the rootbeer ending
elif rootbeer_points > coke_points and rootbeer_points > sprite_points and rootbeer_points > tea_points and rootbeer_points > water_points and rootbeer_points > coffee_points:
     print ("You are rootbeer! you taste how abraham lincon looks... bad")
     #this happens when they get the tea ending
elif tea_points > coke_points and tea_points > sprite_points and tea_points > water_points and tea_points > rootbeer_points and tea_points > coffee_points:
     print ("you are a tea person! 'tea is just hot brown water' - ted lasso")
     #this happens when they get the water ending
elif water_points > coke_points and water_points > sprite_points and water_points > rootbeer_points and water_points > tea_points and water_points > coffee_points:
     print ("You are a water person... water is boring...")
     #this happens when they get the coffee ending
elif coffee_points > coke_points and coffee_points > sprite_points and coffee_points > rootbeer_points and coffee_points > tea_points and coffee_points > water_points:
     print (" you are a coffee person... ew")
else: 
     print ("your a mix! like when you get all of the sodas at the soda fountain!")
     print ("fun but weird!")
