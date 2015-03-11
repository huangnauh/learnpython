#pythonµÝ¹é°æ±¾
def merge(left,right):
    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    while left:
        merged.append(left.pop(0))
    while right:
        merged.append(right.pop(0))
    return merged
    
def merge_sort(a):
    n = len(a)
    if n<= 1:
        return a
    mid = n//2
    return merge(merge_sort(a[:mid]),merge_sort(a[mid:]))