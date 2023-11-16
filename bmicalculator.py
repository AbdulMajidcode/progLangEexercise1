# SCT211-0028/2022
# ABDIMAJID DAKANE MUKTAR

weight = input("Enter your weight: ")
height = input("Enter your height: ")
bmi = int(weight) / float(height)**2
print(bmi)

if bmi < 20:
    print("You are underweight")
elif bmi < 30:
    print("You have normal weight")

else:
    print("You are overweight")