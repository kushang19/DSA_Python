# [Approach - 1] Index Tracking - O(n) Time and O(1) Space - Understood 

# def smallestSubstring(S):
#     res = float("inf")

#     # To check 0, 1 and 2
#     zero = 0
#     one = 0
#     two = 0

#     zeroindex = 0
#     oneindex = 0
#     twoindex = 0
#     for i in range(len(S)):
#         if (S[i] == '0'):
#             zero = 1
#             zeroindex = i

#         elif (S[i] == '1'):
#             one = 1
#             oneindex = i

#         elif (S[i] == '2'):
#             two = 1
#             twoindex = i

#         # Calculating length
#         if (zero and one and two):
#             res = min(res,
#                       max([zeroindex, oneindex, twoindex])
#                       - min([zeroindex, oneindex, twoindex]))
        
#     if (res == float("inf")):
#         return -1
#     return res + 1


# # Driver Code
# S = "01212"

# # Function call
# print(smallestSubstring(S))








# [Approach - 2] Using a sliding window - O(n) Time and O(1) Space - Pending

def smallestSubstring(S):

    # Initialize variables
    n = len(S)
    min_len = float("inf")
    i = 0
    j = 0
    cnt = 0

    # Frequency array
    freq = [0] * 3

    while j < n:
        print(freq[int(S[j])], S[j])
        freq[int(S[j])] += 1
        if freq[int(S[j])] == 1:
            cnt += 1

        if cnt == 3:
            while freq[int(S[i])] > 1:
                freq[int(S[i])] -= 1
                i += 1
            min_len = min(min_len, j - i + 1)
            freq[int(S[i])] -= 1
            i += 1
            cnt -= 1
        j += 1

    return -1 if min_len == float("inf") else min_len

# Driver code
S = "01212"

print(smallestSubstring(S))