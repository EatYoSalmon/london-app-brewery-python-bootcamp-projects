# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)
lifeSpanYear = 90
remainYear = lifeSpanYear - age
remainDay = remainYear * 365
remainWeek = remainYear * 52
remainMonth = remainYear * 12

print(f"You have {remainDay} days, {remainWeek} weeks, and {remainMonth} months left.")


