"""
  Lesson 1: ex3.py
"""

# 1. Print out your favourite food 42 times using * operator.

print("Chocolate" * 42)

# 2. Insert space between each output and print it out again.

print((("Chocolate" + " ") * 42).strip())

# 3. Save your favourite food into a variable and print it out 42 times

favourite_food: str = "Chocolate"
print(((favourite_food + " ") * 42).strip())

# 4. My favourite food is "sushi", save it into a variable and using
#    fast swapping operation change it with your variable.
#    Now your favourite food should be "sushi" and mine will be yours.#

new_favourite_food: str = "Sushi"
favourite_food, new_favourite_food = new_favourite_food, favourite_food
