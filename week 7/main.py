from util.bmi import BMI

the_height = float(input("Enter the height in cm: "))
the_weight = float(input("Enter the weight in kg: "))

print(BMI.bmi_calculator(height=the_height, weight=the_weight))
