# 🧩 Longest Substring with At Most 2 Distinct Characters

def longest_substring_two_distinct(s):
    n = len(s)
    start = 0
    end = 0
    freq = [0] * 256
    max_len = 0
    distinct = 0

    while end < n:
        # Expand the window by adding s[end]
        if freq[ord(s[end])] == 0:
            distinct += 1
        
        freq[ord(s[end])] += 1


        # If more than 2 distinct chars → shrink from start
        while distinct > 2:
            freq[ord(s[start])] -=1
            if freq[ord(s[start])] == 0:
                distinct -= 1
            start += 1

        
        # Update max_len (window is valid)
        window_len = end - start + 1
        if window_len > max_len:
            max_len = window_len

        end +=1
    
    return max_len


# Example:
# s = "abcbbbbcccbdddadacb" # Output: 10 # substring = "bcbbbbcccb"
s = "eceba"  # Final max_len = 3 → substring "ece"
print(longest_substring_two_distinct(s))  






# | Step | start | end | Window | Distinct Chars      | Action              | max_len |
# | ---- | ----- | --- | ------ | ------------------- | ------------------- | ------- |
# | 1    | 0     | 0   | "e"    | {e} → 1             | valid               | 1       |
# | 2    | 0     | 1   | "ec"   | {e, c} → 2          | valid               | 2       |
# | 3    | 0     | 2   | "ece"  | {e, c} → 2          | valid               | 3       |
# | 4    | 0     | 3   | "eceb" | {e, c, b} → 3       | ❌ too many → shrink |         |
# |      | 1     | 3   | "ceb"  | {c, e, b} → still 3 | shrink again        |         |
# |      | 2     | 3   | "eb"   | {e, b} → 2          | ✅ valid again       | 3       |
# | 5    | 2     | 4   | "eba"  | {e, b, a} → 3       | ❌ too many → shrink |         |
# |      | 3     | 4   | "ba"   | {b, a} → 2          | ✅ valid             | 3       |


# Final max_len = 3 → substring "ece"