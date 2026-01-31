# Functions in Python

def greet(name):
    return f"Hello, {name}!"

print(greet("Aaina"))

def add(a, b):
    return a + b

print("Sum:", add(10, 20))

def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("5 is", is_even(5))
