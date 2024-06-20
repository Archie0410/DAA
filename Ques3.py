def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

num = int(input("Enter a number: "))
if num>=0:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
else:
    print("Enter a positive number")