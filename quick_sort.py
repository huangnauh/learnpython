def q_sort(a):
    def q_sort_helper(a,first,last):
        if first<last:
            def partition(a,first,last):
                done = 0
                left = first+1
                right = last
                while not done:
                    while left<=right and a[left] <= a[first]:
                        left += 1
                    while right>=left and a[right] > a[first]:
                        right -= 1
                    if left > right:
                        done = 1
                    else:
                        a[left],a[right] = a[right],a[left]
                        left += 1
                        right -= 1
                a[first],a[right] = a[right],a[first]
                return right
            q = partition(a,first,last)
            q_sort_helper(a,first,q-1)
            q_sort_helper(a,q+1,last)
    q_sort_helper(a,0,len(a)-1)