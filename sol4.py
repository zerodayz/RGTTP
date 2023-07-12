"""
  Lesson 1: ex4.py
"""

# 1. Create a new list with the following values:
#    Apple, Milk, Bread, Chicken and Pasta

shopping_list: list = ["Apples",
                       "Milk",
                       "Bread",
                       "Chicken",
                       "Pasta"]

# 2. Write a check to see if Orange is in the shopping list or not.

if "Orange" in shopping_list:
    print("Orange is in the shopping list.")
else:
    print("Orange is not in the shopping list.")

# 3. Write a function "in_shopping_list" that takes a item such as
#    orange, and returns True or False.
#    Depending whether the item is in the list or not.


def in_shopping_list(name: str) -> bool:
    if name in shopping_list:
        return True
    else:
        return False

# 4. Write a function "show_shopping_list" that will return a
#    shopping list and print it out on the screen.


def show_shopping_list() -> list:
    return shopping_list


print(show_shopping_list())

# 5. Create a list of the following values: 2.99 1.79 3.49 6.99 2.49

prices: list = [2.99, 1.79, 3.49, 6.99, 2.49]

# 6. Create a function price_checker, and pass this list as
#    an argument and let the function return the cheapest price.#


def price_checker(items: list) -> float:
    return min(items)


# 7. Write another function show_price, that will call your
#    price_checker function and uses the result to
#    print the cheapest price.

def show_price():
    lowest_price = price_checker(prices)
    print(lowest_price)


show_price()
