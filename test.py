# ==========================  knapsack problem  ==================================

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
