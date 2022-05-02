'''
Love Calculator
100 Days of Code: The Complete Python Pro Bootcamp 2022 by Angela Yu
Coding Challenge: Day 3 Exercise 5

This is a calculator which shows you the compatablity score
between you and your crush.

It is based on a BuzzFeed article, an extra-idiotic one at that, too.

It calculates the instances of the letters in the word "true" and "love"
of your full name and your crush's full name. Add 2 parts to make a 2 digit integer
as score, then returns a reading based on the score. 

'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

score_t = lower_name1.count("t") + lower_name2.count("t")
score_r = lower_name1.count("r") + lower_name2.count("r")
score_u = lower_name1.count("u") + lower_name2.count("u")
score_e = lower_name1.count("e") + lower_name2.count("e")
score_true = str(score_t + score_r + score_u + score_e)

score_l = lower_name1.count("l") + lower_name2.count("l")
score_o = lower_name1.count("o") + lower_name2.count("o")
score_v = lower_name1.count("v") + lower_name2.count("v")
score_love = str(score_l + score_o + score_v + score_e)

str_score_total = score_true + score_love
int_score_total = int(str_score_total)

if int_score_total < 10 or int_score_total > 90:
  print(f"Your score is {int_score_total}, you go together like coke and mentos.")
elif int_score_total >= 40 and int_score_total <= 50:
  print(f"Your score is {int_score_total}, you are alright together.")
else:
  print(f"Your score is {int_score_total}.")
