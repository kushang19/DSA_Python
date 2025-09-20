# =========================== The Celebrity Problem Using STACK ===========================


# Given a square matrix mat[][] of size n x n, where mat[i][j] == 1 means person i knows person j, and mat[i][j] == 0 means person i does not know person j, find the celebrity person where,

# A celebrity is defined as someone who:

# Is known by everyone else
# Does not know anyone (except themselves)
# Return the index of the celebrity if one exists, otherwise return -1.

# Note: It is guaranteed that mat[i][i] == 1 for all i

# Examples:  

# Input: mat[][] = [[1, 1, 0], 
#                              [0, 1, 0], 
#                              [0, 1, 1]]
# Output: 1
# Explanation: 0th and 2nd person both know 1. Therefore, 1 is the celebrity.

# Input: mat[][] = [[1, 1], 
#                              [1, 1]]
# Output: -1
# Explanation: The two people at the party both know each other. None of them is a celebrity.

# Input: mat[][] = [[1]]
# Output: 0


# Logic: condition to be a celebrity 
# 1. [i] [celebrity] = 1 (i.e i must know the celebrity)
# 2. [celebrity] [i] = 0 (i.e celebrity must not know anyone apart from himself)


def celebrity(mat):
    n = len(mat)
    st = []

    for i in range(n):
        st.append(i)

    while len(st) > 1:
        a = st.pop()
        b = st.pop()

        if mat[a][b]:
            st.append(b)
        else:
            st.append(a)
    c = st.pop()

    for i in range(n):
        if(i != c and (mat[i][c] == 0 or mat[c][i] == 1)):
            return -1
        
    return c
    

mat = [[1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]]
print(celebrity(mat))