print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill ? $"))
number_of_people = float(input("How many people to split the bill ? "))
tip_percentage = float(input("What percentage tip do you want to give ? 10 12 15 ?"))
total = ((total_bill * tip_percentage / 100) + total_bill)/number_of_people
print(f'Each person should pay: ${round(total, 2)}')
