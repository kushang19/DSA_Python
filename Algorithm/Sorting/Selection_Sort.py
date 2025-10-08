# Selection Sort

arr = [3,2,6,8,1]

def selection_sort(a):
    n = len(a)

    print("before: ",a)
    for i in range(n):
        for j in range(i+1,n):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
        print("inside j",a)
    print("after: ",a)  

selection_sort(arr)