# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

stacked_height = 0
headcount = 0
for height in student_heights:
    stacked_height += height
    headcount += 1

avg_height = round(stacked_height / headcount)
print(avg_height)

#Write your code below this row 👇




