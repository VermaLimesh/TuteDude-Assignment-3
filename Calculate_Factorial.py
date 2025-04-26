# Calculate Factorial Using a Function

num = int(input('Enter a Number: '))

def factorial(n):
    if n==1:
     return 1
    else:
     return n * factorial(n-1)

result = factorial(num)

print(f"The factorial of {num} is {result}")

