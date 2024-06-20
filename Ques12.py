import math
def lcm(a, b):
    return abs(a*b)//math.gcd(a, b)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")