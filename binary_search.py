def binary_last_search(alist,item):
	first = -1
	n = len(alist)
	last = n
	while first+1 < last:
		mid = first + (last-first)//2
		if alist[mid] > item:
			last = mid
		else:
			first = mid
	if first < 0 or alist[first] != item:
		return -1
	return first
	

def binary_first_search(alist,item):
	first = -1
	n = len(alist)
	last = n
	while first+1 < last:
		mid = first + (last-first)//2
		if alist[mid] < item:
			first = mid
		else:
			last = mid
	if last >= n or alist[last] != item:
		return -1
	return last
	
def binary_first_search(alist,item):
	first = 0
	n = len(alist)
	last = n
	while first < last:
		mid = first + (last-first)//2
		if alist[mid] < item:
			first = mid+1
		else:
			last = mid
	if first >= n or alist[first] != item:
		return -1
	return first

def binary_last_search(alist,item):
	first = -1
	n = len(alist)
	last = n-1
	while last > first:
		mid = last - (last-first)//2
		if alist[mid] > item:
			last = mid-1
		else:
			first = mid
	if last < 0 or alist[last] != item:
		return -1
	return last


def binary_less_search(alist,item):
	first = -1
	n = len(alist)
	last = n
	while first+1 < last:
		mid = first + (last-first)//2
		if alist[mid] < item:
			first = mid
		else:
			last = mid
	return last-1

def binary_than_search(alist,item):
	first = -1
	n = len(alist)
	last = n
	while first+1 < last:
		mid = first + (last-first)//2
		if alist[mid] > item:
			last = mid
		else:
			first = mid
	if first == n-1:
		return -1
	else:
		return first+1