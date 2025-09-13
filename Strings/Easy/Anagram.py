# Given two non-empty strings s1 and s2 of lowercase letters, determine if they are anagrams — i.e., if they contain the same characters with the same frequencies.
s1 = "anagram"  
s2 = "agramna9"
a = "abcdefghijklmnopqrstuvwxyz"

def anagram(s1, s2, a):
    m = len(s1) 
    n = len(s2)
    q = len(a)
    c1 = [0] * q
    c2 = [0] * q
    
    if m != n:
        return False
    
    for i in range(m):
        for j in range(q):
            if s1[i] == a[j]:
                c1[j] += 1
                break
    for i in range(n):
        for j in range(q):
            if s2[i] == a[j]:
                c2[j] += 1
                break
    print(c1)
    print(c2)
    
    if c1 == c2:
        return True
    else:
        return False

print(anagram(s1, s2, a))