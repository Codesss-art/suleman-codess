def count_vowels(s, index=0):
    if index == len(s):
        return 0
    
    vowels = "aeiouAEIOU"
    
    if s[index] in vowels:
        return 1 + count_vowels(s, index + 1)
    else:
        return count_vowels(s, index + 1)

text = input("Enter string: ")
result = count_vowels(text)
print(f"Number of vowels: {result}")
