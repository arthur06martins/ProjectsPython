# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
calculoImc = weight / (height ** 2)

if calculoImc < 18.5:
  print(f"Your BMI is {calculoImc}, you are underweight.")
elif calculoImc >= 18.5 and calculoImc < 25:
  print(f"Your BMI is {calculoImc}, you have a normal weight.")
elif calculoImc >= 25 and calculoImc< 30:
  print(f"Your BMI is {calculoImc}, you are slightly overweight.")
elif calculoImc >= 30 and calculoImc <35:
  print(f"Your BMI is {calculoImc}, you are obese.")
else:
  print(f"Your BMI is {calculoImc}, you are clinically obese.")