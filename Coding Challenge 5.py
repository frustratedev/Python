# Coding challenge part 5
# Write a function which would divide two numbers, design the function in a manner that it handles the divide by zero exception.

#Input
a = int(input("Enter number here: "))
b = int(input("Enter number here: "))

#Process
def div(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("ERROR: ZERO DIVISION ERROR")
    finally:
        print("FINISHED")

#Output
div(a, b)