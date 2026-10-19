# Iterative method
def iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Recursive method
def recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive(n - 1)

# Main program
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Iterative Factorial:", iterative(n))
    print("Recursive Factorial:", recursive(n))
