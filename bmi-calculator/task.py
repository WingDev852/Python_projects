height = float(input("What is your height in cm? "))
weight = float(input("What is your weight in kg? "))

height_m = height / 100
bmi = weight / (height_m ** 2)

print(f"Your BMI is {round(bmi, 2)}")
