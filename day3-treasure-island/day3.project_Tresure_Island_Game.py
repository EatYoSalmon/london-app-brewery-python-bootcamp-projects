'''
Treasure Island Game
v0.1
by Grich

This is an adventure game where player choose between 2 choices in each stage
in attempt to get to the treasure room and win the game.

Day 3 final project of
100 Days of Code: The Complete Python Pro Bootcamp 2022 by Angela Yu
'''

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Welcome to Treasure Island. Your mission is to find the treasure.")

opt1 = input("\nThere seem to be a split in the trail...\nWhich way do you want to go? 'left' or 'right'? ").lower()

# opt 1 good choice
if opt1 == "left":
  opt2 = input("\nThe trail led you to a secret beach! It seems to connect to that mysterious island but the tide is still high.\nDo you want to 'wait' for low tide, or take a chance and 'swim' across? ").lower()

  # opt 2 good choice
  if opt2 == "wait":
    opt3 = input("\nLow tide came a lot sooner than expected. You walked across the sand bridge to that mysterious island...\nWoah! You came across a colossal castle hidden deep in the jungle while you are exploring the island! The sun is going down and it's getting cold really fast. Do you want to explore the castle 'now' or make a campfire outside and wait till next 'morning'? ").lower()

    # opt 3 good choice
    if opt3 == "now":
      opt4 = input("\nYou went into the castle as the sun is setting. You grab a lit torch hung on the wall as the hall are very dark...\n\nThe long hallway leads you to the end with 2 doors; a 'blue' and a 'red' one. Which door do you wish to open? ").lower()

      # opt 4 good choice      
      if opt4 == "blue":
        print("\nYou push the blue door open and hold up the torch to see what's inside...\n...\nHooray! You've found the treasure room! Now you're going to be the richest man on Earth!\n\n----CONGRATULATION, YOU'VE COMPLETED THE GAME!----")

      # opt 4 bad choice
      else:
        print("\nYou push the red door open and hold up the torch to see what's inside...\n...\n...*low pitch grunt*...\nYou have awakened the Protector! He will punish all those who try to steal the treasure with his thorny mace!\n\nYou tried to escape, but the red door slam shut immediately after the Protector is awakened.\n\n*THUMP!*\n\nThe Protector swings his mace, bashing your skull before you can dodge. As you are slowly losing consciousness, you notice that the door is actually blue, but it's been drenched in the blood of those who were punished by the Protector inside this room...\n\n----GAME OVER---")

    # opt 3 dangerous choice    
    else:
      print("\nAfter several hours of trying, you successfully get the campfire lit... It's pitch black in the jungle at night...\nWait... What's that sound?\n... *high pitch shriek* ...\n*SCREAM*")
      opt3_1 = input("\n\nA giant creature spotted you from the campfire! It's charging towards you at full speed! Quick! Run and 'hide' in the dark jungle or go into the 'castle'? ").lower()

      # opt 3.1 good choice      
      if opt3_1 == 'castle':
        print("\nYou abandon the campfire you put hours of work, blood, sweat, and tear and run for your life towards the castle. As the creature almost catches up to you, you slip past through the main gate. It stops and hesitates to take a step into the castle's domain. It seems to very be scared of something in this castle...")
        #jumpt to opt 4 (now opt 3.2)
        opt3_2 = input("\nYou went into the castle immediately, fearful of the creature. You grab a lit torch hung on the wall as the hall are very dark...\n\nThe long hallway leads you to the end with 2 doors; a 'blue' and a 'red' one. Which door do you wish to open? ").lower()

        # opt 3.2 good choice
        if opt3_2 == "blue":
          print("\nYou push the blue door open and hold up the torch to see what's inside...\n...\nHooray! You've found the treasure room! Now you're going to be the richest man on Earth!\n\n----CONGRATULATION, YOU'VE COMPLETED THE GAME!----")

        # opt 3.2 bad choice
        else:
          print("\nYou push the red door open and hold up the torch to see what's inside...\n...\n...*low pitch grunt*...\nYou have awakened the Protector! He will punish all those who try to steal the treasure with his thorny mace!\n\nYou tried to escape, but the red door slam shut immediately after the Protector is awakened.\n\n*THUMP!*\n\nThe Protector swings his mace, bashing your skull before you can dodge. As you are slowly losing consciousness, you notice that the door is actually blue, but it's been drenched in the blood of those who were punished by the Protector inside this room...\n\n----GAME OVER---")
        
      # opt 3.1 bad choice
      else:
        print("\nYou try to run deeper into the forest away from the creature but- OH SHIT! Because it is so dark, you crashed straight into its den! At least its family get to have a very nice dinner this evening <3\n\n----GAME OVER---")

  # opt 2 bad choice
  else:
    print("\nOh no! You are attacked by a float of saltwater crocodiles!\n\n----GAME OVER----")

# opt 1 bad choice
else:
  print("\nYou fell into a pitfall trap! It's too deep for you to get out!\n\n----GAME OVER----")
