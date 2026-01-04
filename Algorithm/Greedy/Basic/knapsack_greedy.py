# ==========================  knapsack problem  ==================================


# Given two arrays, val[] and wt[], representing the values and weights of item respectively, and an integer capacity representing the maximum weight a knapsack can hold, we have to determine the maximum total value that can be achieved by putting the items in the knapsack without exceeding its capacity.
# Items can also be taken in fractional parts if required.

# Examples:

# Input: val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
# Output: 240 
# Explanation: We will take the items of weight 10kg and 20kg and 2/3 fraction of 30kg. 
# Hence total value will be 60 + 100 + (2/3) * 120 = 240.

# Input: val[] = [500], wt[] = [30], capacity = 10
# Output: 166.667

def fractional_knapsack(p, w, c):
    n = len(p)
    ratio = []

    for i in range(n):
        ratio.append(p[i] / w[i])

    for i in range(n):
        for j in range(i + 1, n):
            if ratio[i] < ratio[j]:
                ratio[i], ratio[j] = ratio[j], ratio[i]
                p[i], p[j] = p[j], p[i]
                w[i], w[j] = w[j], w[i]

    total_profit = 0

    for i in range(n):
        if c == 0:
            break

        if c >= w[i]:
            total_profit += p[i]
            c -= w[i]
        else:
            total_profit += (c / w[i]) * p[i]
            c = 0   # no more space
            break

    return total_profit


# ✅ Test Cases:
print(fractional_knapsack([25, 24, 15], [18, 15, 10], 20))  # ✅ Output: 31.0
print(fractional_knapsack([60, 100, 120], [10, 20, 30], 50)) # ✅ Output: 240.0
