# Check if Permutation of Pattern is Substring

# Given two strings txt and pat having lowercase letters, the task is to check if any permutation of pat is a substring of txt.

# Examples:

# Input: txt = "geeks", pat = "eke"
# Output: true
# Explanation: "eek" is a permutation of "eke" which exists in "geeks".

# Input: txt = "programming", pat = "rain"
# Output: false
# Explanation: No permutation of "rain" exists as a substring in "programming".

txt = 'geeks'
pat = 'eks'

def check_permutation(txt, pat):

    freq1 = [0] * 256
    freq2 = [0] * 256
    # This assumes ASCII characters, which is fine since your question states lowercase letters.
    # If we wanted to be strict and use only lowercase letters, freq1 = [0] * 26 would be enough.
    
    n = len(txt)
    w = len(pat)

    for i in range(w):
        freq1[ord(txt[i])] += 1
        freq2[ord(pat[i])] += 1

    if freq1 == freq2:
        return True
    else:
        for i in range(1,n-w+1):
            print(i)
            freq1[ord(txt[i-1])]-= 1
            freq1[ord(txt[i+w-1])]+= 1
            print(freq1)
            print(freq2)
            print(freq1 == freq2)
            if freq1 == freq2:
                return True
    return False

print("Final Result: ",check_permutation(txt, pat))