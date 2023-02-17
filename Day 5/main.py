student_height = input("Input a list of students height: ").split()
total = 0
average_height = 0
y = 0
for i in student_height:
    student_height[y] = float(student_height[y])
    total += student_height[y]
    y += 1
    average_height = total / y

print(f"The average height of is: {round(average_height)}")

