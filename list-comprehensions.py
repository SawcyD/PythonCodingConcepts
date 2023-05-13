"""
List comprehensions provide a concise way to create lists based on existing lists (or other iterable objects).
They can be very useful and can replace many traditionally written loops, making your code more readable and often faster.

Your task is to complete the following exercises using list comprehensions:

Create a list of squares for all numbers from 0 to 9.
Create a list of all even numbers from 0 to 20.
Given a list of words ["apple", "banana", "cherry"], create a new list that contains the length of each word.
Given a list of numbers [-2, -1, 0, 1, 2], create a new list that contains the absolute value of each number.
Here's a template to get you started:

"""

# Exercise 1
squares = [x ** 2 for x in range (10)]

# Exercise 2
even_numbers = [number for number in range (21) if number % 2 == 0]

# Exercise 3
words = ["apple", "banana", "cherry"]
word_lengths = [len (word) for word in words]

# Exercise 4
numbers = [-2, -1, 0, 1, 2]
absolute_values = [abs (number) for number in numbers]
