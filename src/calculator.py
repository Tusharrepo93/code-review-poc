def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    # TODO: Add error handling
    return a / b

def multiply(a, b):
    result = a * b
    print("Result is: " + str(result))  # Bad practice: print in function
    return result

# Missing docstrings
# No input validation
# Potential division by zero
