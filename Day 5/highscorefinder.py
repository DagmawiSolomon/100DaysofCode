scores = input("Enter scores: ").split()
max_value = 0
for score in range(0,len(scores)):
    scores[score] = int(scores[score])
    if scores[score] > max_value:
        max_value = scores[score]
print(scores)
print(f"The highest score in the class is: {max_value}")
