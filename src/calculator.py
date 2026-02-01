def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    # TODO: This will crash if b is 0!
    return a / b

def multiply(a, b):
    result = a * b
    print("Result is: " + str(result))  # Bad practice
    return result
