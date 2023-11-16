# sct 211-0028/2022
# Abdimajid Dakane Muktar



total_bill = int(input("Enter the total bill amount: "))
tip_percentage = int(input("Enter the tip percentage (10, 12, or 15): "))
number_of_people = int(input("Enter the number of people splitting the bill: "))

# Calculate the tip amount
tip_amount = total_bill * (tip_percentage/ 100)

#total amount per person
total_per_person = (total_bill + tip_amount) / number_of_people

#the total amount per person rounded to 2 d.p
total_amount = round(total_per_person, 2)

# display the output
print(f"Each person should pay: Ksh. {total_amount}")