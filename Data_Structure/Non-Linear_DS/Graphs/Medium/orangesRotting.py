# ======================== Rotten Oranges =====================

# Given an n x m grid, where each cell has the following values : 

# 2 - represents a rotten orange

# 1 - represents a Fresh orange

# 0 - represents an Empty Cell

# Every minute, if a fresh orange is adjacent to a rotten orange in 4-direction ( upward, downwards, right, and left ) it becomes rotten. 

# Return the minimum number of minutes required such that none of the cells has a Fresh Orange. If it's not possible, return -1.


# Example 1
# Input: grid = [ [2, 1, 1] , [0, 1, 1] , [1, 0, 1] ]
# Output: -1
# Explanation: Orange at (3,0) cannot be rotten.

# Example 2
# Input: grid = [ [2,1,1] , [1,1,0] , [0,1,1] ] 
# Output: 4



from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # Step 1: Initialize
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))   # rotten orange
            elif grid[r][c] == 1:
                fresh += 1            # fresh orange

    # No fresh oranges initially
    if fresh == 0:
        return 0

    minutes = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    # Step 2: BFS
    while queue and fresh > 0:
        minutes += 1

        for _ in range(len(queue)):
            # The deque.popleft() method removes and returns the element from the left end (first element) of a deque object.
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

    return minutes if fresh == 0 else -1


print(orangesRotting([
 [2, 1, 1],
 [1, 1, 0],
 [0, 1, 1]
]))