# Write a recursive function to check whether a string is a palindrome

def palindrome(s):
    n = len(s)
    def rev_fun(n):
        if n < 0:
            return ""
        else: 
            return s[n] + rev_fun(n-1)
    r = rev_fun(n-1)
    if s == r:
        return True
    else:
        return False

print("PALINDROME: ", palindrome("madam"))