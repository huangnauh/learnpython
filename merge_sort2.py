#python利用闭包实现就地排序
def merge_sort(a):
    n = len(a)
    if n<=1:
        return
    mid = n//2
    left = a[:mid]
    right = a[mid:]
    merge_sort(left)
    merge_sort(right)
    def merge(left,right):
        i = j = k = 0
        l = len(left)
        r = len(right)
        while j<l and k<r:
            if left[j] <= right[k]:
                a[i] = left[j]
                j+=1
            else:
                a[i] = right[k]
                k+=1
            i += 1
        while j<l:
            a[i] = left[j]
            i += 1
            j += 1
        while k<r:
            a[i] = right[k]
            i += 1
            k += 1
    merge(left,right)