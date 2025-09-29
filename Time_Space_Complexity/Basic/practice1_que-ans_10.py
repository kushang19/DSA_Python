# 1. Simple Loop

def print_numbers(n):
    for i in range(n):
        print(i)


# 2. Nested Loops

def nested_loop(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


# 3. Sequential Loops

def sequential_loops(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j * j)


# 4. Different Loop Variables

def different_loops(n, m):
    for i in range(n):
        print(i)
    
    for j in range(m):
        print(j)


# 5. Logarithmic Complexity

def logarithmic(n):
    i = 1
    while i < n:
        print(i)
        i = i * 2

# 6. Nested Loops with Different Bounds

def nested_different(n, m):
    for i in range(n):
        for j in range(m):
            print(i, j)


# 7. Loop with Step

def loop_with_step(n):
    for i in range(0, n, 5):
        print(i)


# 8. Mixed Complexities

def mixed_complexity(n):
    for i in range(n):
        for j in range(10): # Fixed inner loop
            print(i + j)


# 9. Triple Nested Loops

def triple_loop(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)


# 10. Complexity with a List Operation

def process_list(items):
    while len(items) > 0:
        item = items.pop(0) # Remove the first element
        print(item)


# ====================================== ANSWERS =======================================

# 1. Simple Loop - Answer: O(n)  
# Explanation:
# This is a classic example of linear time complexity. The loop runs n times, and the print operation inside the loop is a constant-time operation, O(1). The total number of operations is directly proportional to the input size n. If n doubles, the number of operations also doubles.


# 2. Nested Loops - Answer: O(n²)
# Explanation:
# This is a classic example of quadratic time complexity. For each iteration of the outer loop i (which runs n times), the inner loop j runs n times. This results in n * n = n² total iterations of the print statement. If n doubles, the number of operations quadruples.


# 3. Sequential Loops - Answer: O(n)
# Explanation:
# The function has two loops that run one after the other (sequentially). The first loop is O(n), and the second loop is also O(n). In Big O notation, we add these together: O(n) + O(n) = O(2n). However, we drop the constant factors, so the final complexity is O(n). The runtime grows linearly with the input size n.


# 4. Different Loop Variables - Answer: O(n + m)
# Explanation:
# Here, the runtime depends on two different input variables, n and m. The first loop runs n times, and the second loop runs m times. These loops are sequential, so we add their complexities. Since we don't know the relationship between n and m, we cannot simplify this further. The complexity remains O(n + m).


# 5. Logarithmic Complexity - Answer: O(log n)
# Explanation:
# This is a classic example of logarithmic time complexity (specifically, base 2). The variable i starts at 1 and doubles with each iteration (i = i * 2). The loop will stop once i is greater than or equal to n. The question is: "How many times can you double 1 until you reach n?" The answer is log₂(n). In Big O notation, we drop the base, so the complexity is O(log n).


# 6. Nested Loops with Different Bounds - Answer: O(n * m)
# Explanation:
# Similar to the simple nested loop, the runtime depends on two different input variables. The outer loop runs n times, and for each of those iterations, the inner loop runs m times. This results in n * m total iterations. Since n and m are independent variables, we express the complexity as their product, O(n * m). If they were the same size, it would simplify to O(n²), but here we must keep them separate.


# 7. Loop with Step - Answer: O(n)
# Explanation:
# Although the loop increments by 5 each time, the number of iterations is still proportional to the input size n. The loop will run approximately n/5 times. In Big O notation, we drop the constant factor (1/5), so the complexity is O(n). The key insight is that the runtime still grows linearly with n; the step size just changes the slope of the line, not the fundamental relationship.


# 8. Mixed Complexities - Answer: O(n)
# Explanation:
# The outer loop runs n times (O(n)). However, the inner loop always runs exactly 10 times, regardless of the input size n. This is a constant-time operation, O(1). When we have nested loops, we multiply their complexities: O(n) * O(1) = O(n). The constant factor of 10 is dropped in Big O notation, leaving us with linear complexity, O(n).


# 9. Triple Nested Loops - Answer: O(n³)
# Explanation:
# This is an extension of the quadratic nested loop. Each loop runs n times, and they are all nested. The total number of iterations is n * n * n = n³. This is cubic time complexity. If n doubles, the number of operations increases by a factor of 8 (2³). The complexity is O(n³).


# 10. Complexity with a List Operation - Answer: O(n²)
# Explanation:
# This is a tricky one! The while loop runs n times (where n is the initial length of the list), which suggests O(n). However, the critical operation is items.pop(0).

# In Python, removing the first element from a list (pop(0)) requires shifting all the remaining elements one position to the front. This shifting operation is an O(n) operation itself.

# Therefore, we have an O(n) operation (pop(0)) inside a loop that runs O(n) times: O(n) * O(n) = O(n²).

# The overall time complexity is quadratic, O(n²), not linear. This is why it's generally inefficient to repeatedly remove elements from the beginning of a large list. Using a collections.deque would make this O(1) per pop from the left, reducing the overall complexity to O(n).