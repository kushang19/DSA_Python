# Sentence Palindrome

# Given a sentence s, determine whether it is a palindrome sentence or not. A palindrome sentence is a sequence of characters that reads the same forward and backward after:

# Converting all uppercase letters to lowercase.
# Removing all non-alphanumeric characters (i.e., ignore spaces, punctuation, and symbols).
# Examples: 

# Input: s = "Too hot to hoot."
# Output: true
# Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters to lowercase, string s will become "toohottohoot" which is a palindrome.




# s = "Too hot to hoot."
s = "Abc 012..## 10cbA"
s = s.lower()

def check_palindrome(s):

    n = len(s)
    start = 0
    end = n-1

    while (start < end):
        if not s[start].isalpha():
            start +=1 
        elif not s[end].isalpha():
            end -=1
        elif s[start].lower() == s[end].lower():
            start +=1
            end -=1
        else:
            return False
        
    return True
        
print(check_palindrome(s))
