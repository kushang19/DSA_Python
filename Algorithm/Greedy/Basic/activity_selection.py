# Activity Selection - manual sort (selection sort) + greedy pick

# Given two arrays start[] and finish[], representing the start and finish times of activities. A person can perform only one activity at a time, and an activity can be performed only if its start time is greater than the finish time of the last chosen activity.
# Find the maximum number of activities that can be performed without overlapping.

# Examples:  

# Input: start[] = [1, 3, 0, 5, 8, 5], finish[] = [2, 4, 6, 7, 9, 9]
# Output: 4
# Explanation: A person can perform at most four activities. The maximum set of activities that can be performed is {0, 1, 3, 4} (these are the indexes in the start[] and finish[] arrays).

# Input: start[] = [10, 12, 20], finish[] = [20, 25, 30]
# Output: 1
# Explanation: A person can perform at most one activity.


# activities = [
#     ['A1', 1, 2],
#     ['A2', 3, 4],
#     ['A3', 0, 6],
#     ['A4', 5, 7],
#     ['A5', 8, 9],
#     ['A6', 5, 9]
# ]

activities = [
    ['A1', 10, 20],
    ['A2', 20, 30],
    ['A3', 12, 25],
    ['A4', 35, 40]
]


def activity_selection(act):
    n = len(act)

    # ---------- Step 1: Sort by finish time (ascending) using selection sort ----------
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if act[j][2] < act[min_idx][2]:  # compare finish times
                min_idx = j
        if min_idx != i:
            act[i], act[min_idx] = act[min_idx], act[i]

    # ---------- Step 2: Greedy selection ----------
    selected = []
    # pick first activity
    selected.append(act[0])          # store the tuple [id, start, finish]
    last_finish = act[0][2]

    # iterate remaining activities
    for k in range(1, n):
        if act[k][1] >= last_finish:
            selected.append(act[k])
            last_finish = act[k][2]

    return selected

picked = activity_selection(activities)

print("Selected activities in order:")
for a in picked:
    print(a)   # prints [id, start, finish]
