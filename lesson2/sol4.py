"""
  Lesson 2: ex4.py
"""

# 1. Print the formatted keys and values of the dictionary.
#    versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}

versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}
for name, version in versions.items():
    print('{0:10} -- {1:10}'.format(name, version))

# 2. Print {} around the version numbers.

for name, version in versions.items():
    print('{0:10} -- {{{1:10}}}'.format(name, version))

# 3. Print numbers in decimal, byte and hexadecimal form.

print("{0:>6} = {0:#16b} = {0:#06x}".format(42))
