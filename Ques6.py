def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

num = int(input("Enter the number of terms: "))
if num>0:
    fib_seq = fibonacci(num)
    print(f"The Fibonacci sequence up to {num} terms is: {fib_seq}")
