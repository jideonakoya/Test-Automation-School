# write a python program that checks if a string is a palindrome.
# Then optionally write a unit test to check your programs correctness

def IsPalindrome(s):
    if (s == s[::-1]):
        return ("The string is a Palindrome")
    else:
        return ("The string is not a Palindrome")

s = 'radar'
print("Palindrome word:", s [::-1])
