# Find the Earliest Repeating Character

# Given a string S of length n, the task is to find the earliest repeated character in it. The earliest repeated character means, the character that occurs more than once and whose second occurrence has the smallest index.

# Example:

# Input: s = "geeksforgeeks" 
# Output: e 
# Explanation: e is the first element that repeats

# Input: s = "hello geeks" 
# Output: l 
# Explanation: l is the first element that repeats

s = "geeksforgeeks" 

def check_repeating_char(s):
    n = len(s)
    res = []
    for i in range(n):
        if (len(res) == 0):
            res.append(s[i])
            continue

        for j in range(len(res)):
            print(s[i],res[j])
            if s[i] != res[j]:
                res.append(s[i])
            else:
                return s[i]
            
    return -1
        

print(check_repeating_char(s), " is the first letter that repeats")

# GFG Method (Recommended): 

a = 'hello'

def check_repeating_char(s):
    n = len(s)
    for i in range(n):
        for j in range(i):
            if s[i] == s[j]:
                return s[i]
            
    return -1
        

print(check_repeating_char(a), " is the first letter that repeats")