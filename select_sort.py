def select_sort(a):
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if a[min] > a[j]:
                min = j
        if min > i :
            a[min],a[i] = a[i],a[min]