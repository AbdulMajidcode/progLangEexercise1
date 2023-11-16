# SCT211-0028/2022
# Abdimajid Dakane Muktar
# age calculator

birth_year = int(input("Enter your year of birth: "))
current_year = int(input("Enter the current year: "))

age = current_year - birth_year
month = age*12
days = age* 365
print("Your are ",age,"years", month,"month",days,"old")


