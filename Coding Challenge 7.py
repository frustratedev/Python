# Coding Challenge 7
# Write Python code which accepts name of a product and in turn returns their respective prices.
# Make sure to use dictionaries to store products and their respective prices.
# The dictionary should include at least 5 elements.

#Dictionary
fruits = {
    "Orange":"5 pesos",
    "Apple":"10 pesos",
    "Grapes":"50 pesos",
    "Guyabano":"100 pesos",
    "Atis":"300 pesos"
}

inptfruit = (input("ENTER FRUIT HERE: "))

if (inptfruit in fruits):
    print(fruits.get(inptfruit))  #From fruit dictionary, get what inptfruit is asking
else:
    print("Fruit not found")
