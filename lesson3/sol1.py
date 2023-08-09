"""
  Lesson 3: ex1.py
"""

# Here is my shopping list:
shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Adding and removing values from a shopping list

shopping_list.append('banana')
print(shopping_list)

# Add chocolate in the third position in your shopping list

shopping_list.insert(2, 'chocolate')
print(shopping_list)

# Extend shopping list by the following items:
# ['chocolate', 'carrot', 'avocado']

shopping_list.extend(['pasta', 'carrot', 'avocado'])

# + Works the same, except it creates new list.
shopping_list + ['pasta', 'carrot', 'avocado']
print(shopping_list)

# Remove chocolate (Removes only first)

shopping_list.remove('pasta')
print(shopping_list)

# Remove last item from the list

shopping_list.pop()
print(shopping_list)

# Remove third item from the list

shopping_list.pop(2)
print(shopping_list)

# Count how many carrots are in the shopping list?

count: int = shopping_list.count('carrot')
print(count)

# Get the index of the chocolate (careful can throw traceback)

try:
    idx: int = shopping_list.index('chocolate')
except ValueError as e:
    print(e)
print("I am supposed to be run after traceback.")

# Using start at index

idx_a: int = shopping_list.index('carrot', 4)
print(idx_a)
