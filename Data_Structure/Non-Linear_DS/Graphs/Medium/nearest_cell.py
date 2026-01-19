# Problem Statement 
# https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1


from collections import deque

def nearest_cell(grid):
    rows, cols = len(grid), len(grid[0])
    
    dist = [[-1] * cols for _ in range(rows)]
    queue = deque()

    # Step 1: Push all 1s into queue
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dist[r][c] = 0
                queue.append((r, c))

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    # Step 2: Multi-source BFS
    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    return dist


# ✅ 0 <= nr < rows and 0 <= nc < cols

# This checks:
# “Is the neighbor inside the grid?”
# Because BFS moves:
# Up
# Down
# Left
# Right
# Without this check → ❌ IndexError



# ✅ dist[nr][nc] == -1

# This means:
# “This neighbor has NOT been visited yet”
# Important:
# BFS guarantees shortest path only if we visit once
# -1 = unvisited
# If we don’t check this:
# Same cell may be updated multiple times
# Distances become wrong
# Performance degrades



# ✅ dist[nr][nc] = dist[r][c] + 1
# This is the key BFS insight:
# Distance to neighbor = distance to current cell + 1
# Why?
# Moving one step (Manhattan distance)
# BFS explores in increasing distance order



# ✅ queue.append((nr, nc))
# This schedules the neighbor to:
# Spread BFS further
# Be processed in the next BFS layer