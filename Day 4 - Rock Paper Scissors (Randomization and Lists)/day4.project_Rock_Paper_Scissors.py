rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player = input("\nYou're playing Rock Paper Scissors against a computer\nWhat do you choose? Enter 0 for Rock, 1 for Paper, 2 for Scissors. ")
print("\nYou choose:")
if player == "0":
  print(rock)
elif player == "1":
  print(paper)
elif player =="2":
  print(scissors)
else:
  print("to make weird hand sign...")

computer = str(random.randint(0,2))
print("\nComputer choose:")
if computer == "0":
  print(rock)
elif computer == "1":
  print(paper)
else:
  print(scissors)

result = player + computer
if result == "02" or result == "10" or result == "21":
  print("You win!")
elif result == "01" or result == "12" or result == "20":
  print("You lose!")
elif result == "00" or result == "11" or result == "22":
  print("It's a draw...")
else:
  print("You've entered an invalid number.\nThat's a foul so you lost buy default...\n\nYou dingus ;P")
