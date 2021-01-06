# Coding Challenge 13
# Using the concept of operator overloading in Python, change the behavior of the multiplication operator in a way that multiplication operator behaves like an addition operator.
class Multi:
    def __init__(self,x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return x

number_a  = Multi(5)
number_b = Multi(4)

print(number_a * number_b)