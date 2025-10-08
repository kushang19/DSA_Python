# 🧠 What Bubble Sort Actually Does

# 👉 Bubble Sort repeatedly compares adjacent elements (a[j] and a[j+1]) and swaps them if they are in the wrong order.

# After every full pass, the largest element “bubbles up” to the end of the array.

# So, after 1st pass → largest is at end
# after 2nd pass → 2nd largest is second last, and so on.

arr = [3, 2, 6, 8, 1, 4]

def bubble_sort(a):
    n = len(a)

    print("before: ",a)
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
        print("inside j", a)
    print("after: ",a)  

bubble_sort(arr)