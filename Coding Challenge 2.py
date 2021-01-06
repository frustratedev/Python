#Coding Challenge 2
# Create a list of your favorite food items, the list should have minimum 5 elements.
# List out the 3rd element in the list.
# Add additional item to the current list and display the list.
# Insert an element named tacos at the 3rd index position of the list and print out the list elements.

food = ["Steak", "Burger", "Wings", "Pizza", "Fries"]
print(food[2])
food.append("BBQ")
print(food)
food.insert(3, "Tacos")
print(food)
