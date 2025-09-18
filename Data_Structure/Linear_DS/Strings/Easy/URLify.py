# Input: s = "i love programming"
# Output: "i%20love%20programming"
# Explanation: The 2 spaces are replaced by '%20'

# Input: s = "ab cd"
# Output: "ab%20cd"

s = "i love programming"
b = "i%20love%20programming"

def urlIfy(s):
    n = len(s)
    res = ""
    for i in range(n):
        if s[i] == " ":
            res += "%20"
            continue
        res += s[i]
    return res
    
print(urlIfy(s))
print(b)

