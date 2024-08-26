# calculator.py


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Basic Calculator")
    print(f"Addition: {add(5, 3)}")
    print(f"Subtraction: {subtract(5, 3)}")
    print(f"Multiplication: {multiply(5, 3)}")
    print
