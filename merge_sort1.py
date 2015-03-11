#python迭代版本
def merge(left,right):
    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    while left:
        merged.append(left.pop(0))
    while right:
        merged.append(right.pop(0))
    return merged

def iter_mergesort(a):
    lst = [[i] for i in a]
    while len(lst)>1:
        lst.append(merge(lst.pop(0),lst.pop(0)))
    return lst.pop()