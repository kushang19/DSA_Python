# ==================== Job Sequencing Problem ====================

jobs = [
    ['A', 2, 100],
    ['B', 1, 19],
    ['C', 2, 27],
    ['D', 1, 25],
    ['E', 3, 15]
]

n = len(jobs)

# --------- Step 1: Sort jobs by profit in descending order ---------
for i in range(n):
    for j in range(i+1, n):
        if jobs[i][2] < jobs[j][2]:   # compare profits
            jobs[i], jobs[j] = jobs[j], jobs[i]

print("Jobs sorted by profit:")
for job in jobs:
    print(job)

# --------- Step 2: Find max deadline to know how many slots ---------
max_deadline = 0
for i in range(n):
    if jobs[i][1] > max_deadline:
        max_deadline = jobs[i][1]

slots = [-1] * (max_deadline + 1)   # 1-based indexing

total_profit = 0

# --------- Step 3: Place each job in latest possible slot ---------
for i in range(n):
    job_id, deadline, profit = jobs[i]

    # find free slot before or equal to deadline
    for j in range(deadline, 0, -1):
        if slots[j] == -1:
            slots[j] = job_id
            total_profit += profit
            break

print("\nFinal job schedule (by slot):")
for i in range(1, len(slots)):
    print(f"Slot {i}: {slots[i]}")

print("\nTotal Profit:", total_profit)
