# =========================  Sliding Window Technique (fixed-size window) ===============================

# Sliding Window Technique is a method used to solve problems that involve subarray or substring or window.

# Instead of repeatedly iterating over the same elements, the sliding window maintains a range (or “window”) that moves step-by-step through the data, updating results incrementally.
# The main idea is to use the results of previous window to do computations for the next window.
# Commonly used for problems like finding subarrays with a specific sum, finding the longest substring with unique characters, or solving problems that require a fixed-size window to process elements efficiently.



# Using sliding window technique whos window size is 4 find the max value of a sub array
arr = [3,8,2,5,7,6,12]
n = len(arr)
w = 4
max = 0
for i in range(w):
    max += arr[i]
current = max

for i in range(1,n-w+1):
    current = current - arr[i-1] + arr[i+w-1]
    if(current > max):
        max = current

print("MAX of sub array is: ",max)