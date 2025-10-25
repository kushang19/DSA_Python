# Longest substring without repeating characters (variable-size window on string)

def longest_unique_substring(s):
    n = len(s)
    max_len = 0
    start = 0
    freq = [0] * 256  # assuming ASCII chars (0–255)

    for end in range(n):
        freq[ord(s[end])] += 1

        while freq[ord(s[end])] > 1:
            freq[ord(s[start])] -= 1
            start += 1

        window_length = end + start - 1
        if window_length > max_len:
            max_len = window_length
    # print(freq)
    return max_len


# Test
s = "abca"
print(longest_unique_substring(s))  # Output: 3




# 🪄 Step-by-step “Animation” of "abca"


# | Step | `end` | `s[end]` | Window (s[start:end]) | `freq` changes            | Action                             | `max_len` |
# | ---- | ----- | -------- | --------------------- | ------------------------- | ---------------------------------- | --------- |
# | 1    | 0     | 'a'      | `'a'`                 | freq['a']=1               | no duplicate                       | 1         |
# | 2    | 1     | 'b'      | `'ab'`                | freq['b']=1               | no duplicate                       | 2         |
# | 3    | 2     | 'c'      | `'abc'`               | freq['c']=1               | no duplicate                       | 3         |
# | 4    | 3     | 'a'      | `'abca'`              | freq['a']=2 ⚠️ duplicate! | start=0 → remove 'a' (freq['a']=1) | 3         |

