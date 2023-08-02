"""
  Lesson 2: ex2.py
"""

# 1. Use string formatting with empty curly brackets {}
#    to take the argument passed into format and print a
#    sentence of your choice.

argument: str = "amazing"
print("This is {}!".format(argument))

# 2. Use string formatting with positional arguments and
#    print the sentence: "Don't Panic!"

print("{} {}!".format("Don't", "Panic"))

# 3. Use string formatting with named arguments and
#    print the sentence: "[name] is really [what]!" and
#    fill in the brackets with your name and "great".

name = "Simon"
what = "great"
print("{name} is really {what}!".format(name=name, what=what))
