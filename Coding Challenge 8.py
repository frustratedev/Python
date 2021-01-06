# Coding Challenge 8
# List out  all the odd numbers from 1 to 100 using lists in Python.

for x in range(1, 101): #STOP:101 - START:1 = 100
    if x % 2 != 0: #If it is not divisible by 2, then it is an odd number.
        print(x)
