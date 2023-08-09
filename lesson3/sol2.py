from typing import Any
"""
  Lesson 3: ex2.py
"""

# 1. Iterating over the list

my_list: list[Any] = []

for i in range(10):
    my_list.append(i)

print(my_list)

my_list = [i for i in range(10)]
print(my_list)

my_list = []

for i in range(10):
    my_list.append(i**2)

print(my_list)

my_list = [i**2 for i in range(10)]
print(my_list)

my_list = [[i, i**2] for i in range(10)]
print(my_list)

my_list = [[i, i**2, i**3] for i in range(10)]
print(my_list)

# Add conditions

my_list = [[i, i**2, i**3] for i in range(10) if i % 2]
print(my_list)

# Nesting

my_list = []

for i in 'xyz':  # type: ignore
    tmp_list: list[str] = []
    for j in 'abcde':
        tmp_list.append(i+j)  # type: ignore
    my_list.append(tmp_list)

print(my_list)

my_list = [[j+i for i in 'abcde'] for j in 'xyz']
print(my_list)
