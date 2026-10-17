CONTRIBUTORS = ["ALIYU HYDAR AHMAD", "Rachid Abou Djamal Hamadou", "Adithya Panjiyara", "Aaryan Anand Dhorey"] # Conflicts generator 1
 
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print(f"Welcome to the Group Calculator!, written by {CONTRIBUTORS}")
    print(divide(4, 2))
    print(multiply(2, 2)) 
    print(add(2, 2))
    print(subtract(5, 3))
