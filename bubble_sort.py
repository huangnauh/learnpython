def bubble_sort(a):
    n = len(a)
    flag = n-1
    while flag:
        i = flag
        flag = 0
        for j in range(i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                flag = j