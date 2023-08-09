"""
  Lesson 3: ex4.py
"""

# 1. Create your own Shopping List type.
#
# a. Initialize the ShoppingList class with shopping_list
#    shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']
#
# b. Add in_list method, that checks if the item is in list or not,
#    use the format() or f-strings to return the string based on truth:
#    - 'apples' is in the shopping list.
#    - 'apples' not in the shopping list.
#
# c. Add special function when printing the list to output:
#    * Replace the list with {} and print using format().
#    My shopping list: ['apples', 'milk', 'bread', 'carrot', 'pasta']
#
# d. Add special function for comparison of two objects to output:
#    * Based on the truth.
#    - True
#    - False


class ShoppingList(object):
    def __init__(self):
        self.shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']

    def __str__(self) -> str:
        return "My shopping list: {}".format(self.shopping_list)

    def __repr__(self) -> str:
        return "My shopping list: {}".format(self.shopping_list)

    def in_list(self, item: str) -> str:
        if item in self.shopping_list:
            return f"'{item}' is in the shopping list."
        else:
            return f"'{item}' not in the shopping list."

    def __eq__(self, other) -> bool:
        return self.shopping_list == other.shopping_list


monday: ShoppingList = ShoppingList()
print(monday.in_list('apples'))
print(ShoppingList.in_list(monday, 'apples'))

tuesday: ShoppingList = ShoppingList()

print(monday == tuesday)
