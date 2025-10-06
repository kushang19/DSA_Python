# Check if Strings Are Rotations of Each Other

# Given two strings s1 and s2 of equal length, determine whether s2 is a rotation of s1.
# A string is said to be a rotation of another if it can be obtained by shifting some leading characters of the original string to its end without changing the order of characters.

# Examples: 

# Input: s1 = "abcd", s2 = "cdab"
# Output: true
# Explanation: After 2 right rotations, s1 will become equal to s2.

# Input: s1 = "aab", s2 = "aba"
# Output: true
# Explanation: After 1 left rotation, s1 will become equal to s2.

# Input: s1 = "abcd", s2 = "acbd"
# Output: false
# Explanation: Strings are not rotations of each other.

# s1 = "abcd"
# s2 = "cdab"

# s1 = "aab" 
# s2 = "aba"

s1 = "abcd"
s2 = "acbd"

def check_rotation(s1,s2):
    # print(s1, s2)
    n = len(s1)
    s3=""

    for i in range(n):
        for j in range(n):
            if j != n-1:
                s3 += (s1[j+1])
        s3 += (s1[0])
        print(s1,s3)
        if s3 == s2:
            print("Match Found")
            return
        else:
            s1 = s3
            s3 = ""
    print("No Match Found")
    
check_rotation(s1,s2)