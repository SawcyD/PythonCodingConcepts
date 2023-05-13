"""
Your challenge: Write a Python program with a function that takes a string as an argument.
The function should check if a function with that name exists. If it does, it should call that function.
If it does not, it should create a new function with that name that prints the string
"Hello, I am (function name)!" when called. This is your chance to explore Python's dynamic nature further.
Remember, don't look for the answer, try to build it yourself based on the concepts you've learned. Good luck!
"""

def check_function_exists(function_name):
    if function_name in globals():
        globals()[function_name]()
    else:
        globals()[function_name] = lambda: print(f"Hello, I am {function_name}!")

check_function_exists("function_one")
check_function_exists("function_two")

function_one()
function_two()
