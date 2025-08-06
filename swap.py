# Simple swap of two numbers in Python

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Swapping using a temporary variable
temp = a
a = b
b = temp

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
