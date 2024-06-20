def is_palindrome(s):
    return s == "".join(reversed(s))

str = input("Enter a string: ")
if is_palindrome(str):
    print(f"'{str}' is a palindrome.")
else:
    print(f"'{str}' is not a palindrome.")
    