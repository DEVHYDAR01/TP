
CONTRIBUTORS = ["Aaryan Anand Dhorey"]


def add(a, b):
    pass


def subtract(a, b):
    return a - b


def multiply(a, b):
    pass


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print(f"Welcome to the Group Calculator!, written by {CONTRIBUTORS}")
    print(divide(4, 2))
    print(subtract(5, 3))
