"""
  Lesson 3: ex3.py
"""

# Here is my shopping list:
shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Sorting the list

# Built-in function sorted() sorts and return new list

sorted_shopping_list = sorted(shopping_list)
print(shopping_list)
print(sorted_shopping_list)

# .sort() method on list class which performs in-place sorting
shopping_list.sort()
print(shopping_list)

# Built-in function reversed() reverse and return new list

reversed_shopping_list = reversed(shopping_list)
print(shopping_list)
print(reversed_shopping_list)

# The reversed() needs to be converted back to list using list()

reversed_shopping_list = list(reversed(shopping_list))  # type: ignore
print(reversed_shopping_list)

# But if you need this, you should always use sort() and sorted() function with
# argument reverse=True

print(shopping_list)
shopping_list = sorted(shopping_list, reverse=True)
print(shopping_list)

print(shopping_list)
shopping_list.sort(reverse=True)
print(shopping_list)
