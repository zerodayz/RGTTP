"""
  Lesson 2: ex3.py
"""

# 1. Create a list containing three elements representing the
#    name, age, and occupation of a person.
#    Then, print the sentence using the elements with .format()


person_info = ["John Doe", 35, "Engineer"]

print("My name is {}. I am {} years old, and I work as an {}."
      .format(person_info[0], person_info[1], person_info[2]))

# 2. The dictionary should contain keys such as
#    'title', 'author', and 'publication_year'.
#    Use the .format() method with multiple positional arguments.
#    Example:
#    "The guidebook [title] by [author] was published in [publication_year]."

book_info = {
    'title': 'The Hitchhiker\'s Guide To The Galaxy',
    'author': 'Ford Prefect',
    'publication_year': 2023
}

print("The book '{0}' by {1} was published in {2}."
      .format(book_info['title'],
              book_info['author'],
              book_info['publication_year']))


# 3. The dictionary should hold details about a spaceship, such as
#    'name', 'type', and 'purpose'.
#    Use the .format() method with named arguments.
#    Example:
#    "The spaceship is called the [name]. It is a [type] used for [purpose]."

spaceship_info = {
    'name': 'Heart of Gold',
    'type': 'exploration',
    'purpose': 'traveling through space'
}

print(("The spaceship is called the '{name}'. It is a '{type}'"
      + " used for {purpose}.").format(**spaceship_info))
