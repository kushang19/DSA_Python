# Check if two strings are k-anagrams or not
# Changes Needed = string_length - common_characters

s1 = "geeks"
s2 = "eggkf"
a = "abcdefghijklmnopqrstuvwxyz"
k = 1

def kAnagram(s1,s2,k,a):
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
                print(c1)

    for i in range(n):
        for j in range(q):
            if s2[i] == a[j]:
                c2[j] += 1
                print(c2)

    c3 = [0] * q
    c4 = 0


    for i in range(q):
        if c1[i] > c2[i]:
            c3[i] = c2[i]
            c4 += c2[i]
        else:
            c3[i] = c1[i]
            c4 += c1[i]

    print(c3)
    print(c4)
    
    calc = m - c4
    print(calc)

    if calc <= k:
        print("K-anagrams")
    else:
        print("NOT K-anagrams")

kAnagram(s1,s2,k,a)