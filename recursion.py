"""
In computer science, a common method to solve problems is to divide them into smaller subproblems of the same type, a technique known as "recursion".

You're given a task to write a Python function that uses recursion to calculate the factorial of a number.
A factorial of a number n (written as n!) is the product of all positive integers less than or equal to n.
For example, the factorial of 5 (5!) is 12345 = 120.

"""


def factorial (n):
	if n == 0:
		return 1
	else:
		return n * factorial (n - 1)


print (factorial (5))
