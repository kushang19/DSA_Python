# ============================= Introduction to Recursion =========================

# The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called a recursive function.

# A recursive algorithm takes one step toward solution and then recursively call itself to further move. The algorithm stops once we reach the solution.
# Since called function may further call itself, this process might continue forever. So it is essential to provide a base case to terminate this recursion process.

# Steps to Implement Recursion

# Step1 - Define a base case: Identify the simplest (or base) case for which the solution is known or trivial. This is the stopping condition for the recursion, as it prevents the function from infinitely calling itself.

# Step2 - Define a recursive case: Define the problem in terms of smaller subproblems. Break the problem down into smaller versions of itself, and call the function recursively to solve each subproblem.

# Step3 - Ensure the recursion terminates: Make sure that the recursive function eventually reaches the base case, and does not enter an infinite loop.

# Step4 - Combine the solutions: Combine the solutions of the subproblems to solve the original problem.

# ============== Factorial =======================

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))
# print(factorial(6))
# print(factorial(7))

# ============== Fibonacci sequence ==============

# f(0) = 0
# f(1) = 1
# f(2) = f(0) + f(1) = 0 + 1 = 1
# f(3) = f(1) + f(2) = 1 + 1 = 2
# f(4) = F(2) + f(3) = 1 + 2 = 3
# f(n) = f(n-1) + f(n-2)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144....

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

# print("Fibonacci ==>", fibonacci(6))


# ================ find sum of N natural numbers ============

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
    
print("Sum of N natural numbers ", sum(5))



# ============ Practice Questions for Recursion | Set 1 ============

def fun1(x,y):
    if x == 0:
        return y
    else:
        return fun1(x-1, x+y)

print("----", fun1(5,2),"----")