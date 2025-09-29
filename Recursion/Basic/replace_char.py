# Replace all occurrences of a character in a string recursively

# Input: s = "banana", replace 'a' with 'x' → Output: "bxnxnx"

def char_checker(char,n,s,count,k):
    if count > n:
        return k
    else:
        if s[count] == char:
            k += "x"
        else:
            k += s[count]
        return char_checker(char,n,s,count+1,k)

s = "banana"
k =""
char = "a"
n = len(s) - 1
count = 0
print(char_checker(char,n,s,count,k))