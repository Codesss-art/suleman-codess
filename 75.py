def is_palindrome(s, left, right):
    if left >= right:
        return True
    
    if s[left] != s[right]:
        return False
    
    return is_palindrome(s, left + 1, right - 1)

text = input("Enter string: ")
text = text.replace(" ", "").lower()

if is_palindrome(text, 0, len(text) - 1):
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")
