"""
Problem: You're writing a piece of software that needs to log the execution time of certain functions for performance testing.
You decide to use decorators, a powerful Python feature, to implement this without having to modify the functions themselves.

Your task is to write a decorator named log_execution_time that will log (print) the time it takes for a function to execute.
"""
import time

def log_execution_time(func):
    def functionLogger():
        startTime = time.time()
        print(f"Time Before {startTime}")
        func()
        endTime = time.time()
        print(f"Time After {endTime}")
        print(f"Execution Time: {endTime - startTime} seconds")
    return functionLogger

@log_execution_time
def slow_function():
    time.sleep(3)

slow_function()
