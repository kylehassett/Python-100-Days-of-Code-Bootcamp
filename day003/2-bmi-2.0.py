# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height ** 2))

message = ""
if bmi < 18.5:
    message += "are underweight"
elif bmi >= 18.5 and bmi < 25:
    message += "have a normal weight"
elif bmi >= 25 and bmi < 30:
    message += "are slightly overweight"
elif bmi >= 30 and bmi < 35:
    message += "are obese"
else:
    message += "are clinically obese"

print(f"Your BMI is {bmi}, you {message}.")
