"""
  Lesson 2: ex1.py
"""

# 1. Create a format string to display the name and age of a person.

name: str = "Ford Prefect"
age: int = 200
print("{} is {} years old.".format(name, age))

# 2. Print version with it's corresponding upstream codename,
#    and use padding aligned format to left, centre and right.

versions: list[tuple] = [("Stein", "15"), ("Train", "16"), ("Wallaby", "17")]

for version in versions:
    print("{:<10} {:^20} {:>10}".format(version[0], version[1], version[0]))

# 3. Show different representations of an integer.

number: int = 42
print("Decimal: {0}, Binary: {0:b}, Octal: {0:o}, Hexadecimal: {0:x}"
      .format(number))

# 4. Format a floating-point number with fixed precision.

temperature: float = 12.345
print("Temperature: {:.2f}".format(temperature))
