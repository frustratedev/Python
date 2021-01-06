#Coding Challenge 4

# Create a BMI calculator, BMI which stands for Body Mass Index can be calculated using the formula:
# BMI = (weight in Kg)/(Height in Meters)^2.
# Write python code which can accept the weight and height of a person and calculate his BMI.

# note: Make sure to use a function which accepts the height and weight values and returns the BMI value.

#Input
w = float(input("Enter weight here: "))
h = float(input("Enter height here: "))

def BMI(w, h): #Always ensure that your function has parameters
    return (w)/(h) ** 2 #Formula (Process)

#Output
massIndex = BMI(w, h)
print(massIndex)