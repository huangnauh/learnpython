def shell_sort(a):
    n = len(a)
    gap = n//2
    while gap:
        for i in range(gap,n):
            j = i
            temp = a[i]
            while j>gap-1 and a[j-gap]>temp:
                a[j] = a[j-gap]
                j -= gap
            a[j] = temp
        gap = gap // 2