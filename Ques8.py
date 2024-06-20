def sum_of_digits(n):
    return sum(map(int, str(n)))

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"The sum of digits of {num} is {result}")