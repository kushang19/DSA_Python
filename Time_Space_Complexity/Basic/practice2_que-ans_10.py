# https://chat.deepseek.com/a/chat/s/32dca4b2-8a91-4122-b047-381fb644f35f

# 1. Recursive Function with Multiple Calls


def recursive_tree(n):
    if n <= 1:
        return
    print(n)
    recursive_tree(n - 1)
    recursive_tree(n - 1)

# 1. Recursive Function with Multiple Calls - Answer: O(2ⁿ)
# Explanation:
# This creates a binary recursion tree. At each call (except the base case), the function makes 2 recursive calls. The depth of the recursion tree is n. The total number of nodes in such a binary tree is roughly 2ⁿ, and each node does O(1) work (just the print statement). This results in exponential time complexity O(2ⁿ).

# Input: n = 3

# recursive_tree(3)
# │
# ├── print(3)
# ├── recursive_tree(2)
# │   │
# │   ├── print(2)
# │   ├── recursive_tree(1) → returns (base case)
# │   └── recursive_tree(1) → returns (base case)
# │
# └── recursive_tree(2)
#     │
#     ├── print(2)
#     ├── recursive_tree(1) → returns (base case)
#     └── recursive_tree(1) → returns (base case)

# Total operations: 1 (n=3) + 2 (n=2) + 4 (n=1 base cases) = 7 operations
# Pattern: For n=3: 2³ - 1 = 7 operations → O(2ⁿ)
# This is called Exponential Time Complexity.




# 2. Recursive Function with Halving

def recursive_halve(n):
    if n <= 1:
        return
    print(n)
    for i in range(n):
        print(i, end=" ")
    print()
    recursive_halve(n // 2)

# Input: n = 8

# Step-by-step execution:

# Level 0: n=8
# - Print 8
# - Loop: 0 1 2 3 4 5 6 7 (8 operations)
# - Call recursive_halve(4)

# Level 1: n=4  
# - Print 4
# - Loop: 0 1 2 3 (4 operations)
# - Call recursive_halve(2)

# Level 2: n=2
# - Print 2
# - Loop: 0 1 (2 operations)
# - Call recursive_halve(1)

# Level 3: n=1 → base case, return


# Total operations: 8 + 4 + 2 = 14
# Pattern: n + n/2 + n/4 + ... ≈ (n/(1-1/2)) = 2n → O(n) 





# 3. Nested Loops with Logarithmic Inner Loop

def nested_log(n):
    for i in range(n):
        j = 1
        while j < n:
            print(i, j)
            j = j * 2

# Input: n = 8

# Step-by-step execution:

# Outer loop: i = 0 to 7 (8 iterations)

# For each i:
#   j = 1 → print(0,1)
#   j = 2 → print(0,2) 
#   j = 4 → print(0,4)
#   j = 8 → stop (j < 8 is false)
  
# Same pattern for i=1 to i=7:
#   Each has 3 print operations

# Total operations: 8 outer × 3 inner = 24
# Pattern: n × log₂n → O(n log n)





# 4. String Building with Slicing

def build_string(n):
    result = ""
    for i in range(n):
        result += "a"
    return result

# input = 4

# Iteration 1: result = "" + "a" → copy 0 chars + 1 new = 1 copy
# Iteration 2: result = "a" + "a" → copy 1 char + 1 new = 2 copies  
# Iteration 3: result = "aa" + "a" → copy 2 chars + 1 new = 3 copies
# Iteration 4: result = "aaa" + "a" → copy 3 chars + 1 new = 4 copies

# Note :
# result += "a"

# Python does not append directly to the existing string.
# Instead, it creates a new string by copying the old one and adding the new character — which takes O(k) time, where k is the current length of result.

# O(1 + 2 + 3 + ... + n) = O(n(n + 1) / 2) = **O(n²)**

# ✅ Final Answer
# Time Complexity: O(n²)
# Space Complexity: O(n) (for storing the final string)





# 5. Recursive Function with Loop

def recursive_with_loop(n):
    if n <= 0:
        return
    print(f"Level {n}")
    for i in range(n):
        print(i, end=" ")
    print()
    recursive_with_loop(n - 1)

# Input = 4

# Step-by-step execution:

# Level 4: print "Level 4", loop: 0 1 2 3 (4 operations)
# Level 3: print "Level 3", loop: 0 1 2 (3 operations)  
# Level 2: print "Level 2", loop: 0 1 (2 operations)
# Level 1: print "Level 1", loop: 0 (1 operation)
# Level 0: base case

# Total operations: 4 + 3 + 2 + 1 = 10
# Pattern: n(n+1)/2 → O(n²)




# 8. Multiple Recursive Calls with Different Parameters
# Input: n = 4

def multiple_recursive(n):
    if n <= 1:
        return 1
    print(n)
    return multiple_recursive(n - 1) + multiple_recursive(n - 2)

# Step-by-step execution:

# multiple_recursive(4)
# │
# ├── print(4)
# ├── multiple_recursive(3)
# │   │
# │   ├── print(3)
# │   ├── multiple_recursive(2)
# │   │   │
# │   │   ├── print(2)
# │   │   ├── multiple_recursive(1) → 1
# │   │   └── multiple_recursive(0) → 1
# │   │
# │   └── multiple_recursive(1) → 1
# │
# └── multiple_recursive(2)
#     │
#     ├── print(2)
#     ├── multiple_recursive(1) → 1
#     └── multiple_recursive(0) → 1


# Total print operations: 1 (n=4) + 1 (n=3) + 2 (n=2) = 4
# Pattern: Exponential growth → O(2ⁿ)





# 9. Nested Loop with Multiplication
# Input: n = 8

def nested_multiplication(n):
    for i in range(1, n):
        j = 1
        while j < n:
            print(i, j)
            j = j * i
            if i == 1:
                break

# Step-by-step execution:

# i=1: j=1 → print(1,1) → break (1 iteration)
# i=2: j=1,2,4 → print(2,1),(2,2),(2,4) → j=8 stop (3 iterations)
# i=3: j=1,3 → print(3,1),(3,3) → j=9 stop (2 iterations)
# i=4: j=1,4 → print(4,1),(4,4) → j=16 stop (2 iterations)
# i=5: j=1,5 → print(5,1),(5,5) → j=25 stop (2 iterations)
# i=6: j=1,6 → print(6,1),(6,6) → j=36 stop (2 iterations)  
# i=7: j=1,7 → print(7,1),(7,7) → j=49 stop (2 iterations)

# Total iterations: 1 + 3 + 2 + 2 + 2 + 2 + 2 = 14
# Pattern: Roughly n log n → O(n log n)





# 10. Complex Loop Structure
# Input: n = 8

def complex_loop(n):
    i = 1
    while i <= n:
        for j in range(i):
            print(j, end=" ")
        print()
        i = i * 2
        
    for k in range(n):
        print(k, end=" ")



# Step-by-step execution:
# First part (geometric):
# i=1: print 0 (1 element)
# i=2: print 0 1 (2 elements)  
# i=4: print 0 1 2 3 (4 elements)
# i=8: print 0 1 2 3 4 5 6 7 (8 elements)
# Total first part: 1 + 2 + 4 + 8 = 15

# Second part:
# k=0 to 7: print 0 1 2 3 4 5 6 7 (8 elements)

# Total operations: 15 + 8 = 23
# Pattern: 2n + n = 3n → O(n)

