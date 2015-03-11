def insert_sort(a):
    n = len(a)
    for i in range(1,n):
        j = i
        temp = a[i]
        while j>0 and a[j-1]>temp:
            a[j] = a[j-1]
            j -= 1
        a[j] = temp