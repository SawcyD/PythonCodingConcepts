"""
Exceptions are events that occur during the execution of programs that disrupt the normal flow of the program's instructions.
In Python, exceptions can be handled using a try/except block.

You're given a task to write a Python function that takes a list and an index as input and returns the element at that index in the list.
If the index is out of range, your function should raise an IndexError with a custom error message.

"""


def get_element (lst, index):
	try:
		return lst [index]
	except IndexError:
		raise IndexError("Index out of range.")
		# return f"An Error Has Occurred: {e}"


print (get_element ([1, 2, 3], 5))
