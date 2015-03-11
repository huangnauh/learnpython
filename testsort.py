from random import sample
from time import time
import heapq
def bubble_sort(seq):
	n = len(seq)
	flag = n
	while flag:
		i = flag
		flag = 0
		for j in range(1,i):
			if seq[j-1] > seq[j]:
				seq[j-1],seq[j] = seq[j],seq[j-1]
				flag = j
                
def BubbleSort1(seq):
	length = len(seq)
	flag = True
	i = length
	while flag:
		flag = False
		for j in range(1,i):
			if  seq[j-1] > seq[j]:
				seq[j-1],seq[j] = seq[j],seq[j-1]
				flag = True
		i -= 1
        
def BubbleSort2(seq):
	length = len(seq)
	flag = length
	i = length
	while flag:
		i = flag
		flag=0
		for j in range(1,i):
			if  seq[j-1] > seq[j]:
				seq[j-1],seq[j] = seq[j],seq[j-1]
				flag = j
				
def selection_sort(seq):
	n = len(seq)
	for i in range(n):
		mindex = i
		for j in range(i+1,n):
			if seq[mindex] > seq[j]:
				mindex = j
		if mindex > i:
			seq[i],seq[mindex] = seq[mindex], seq[i]

def SelectSort(seq):
	length = len(seq)
	for i in range(length):
		mini = min(seq[i:])
		if seq[i] > mini:
			j = seq.index(mini,i)
			seq[i],seq[j]=seq[j],seq[i]

def SelectSort1(seq):
	length = len(seq)
	for i in range(length):
		minPos = i
		for j in range(i+1,length):
			if seq[minPos] > seq[j]:
				minPos = j
		seq[i],seq[minPos]=seq[minPos],seq[i]            
            
def insertion_sort(seq):
	n = len(seq)
	for i in range(1,n):
		tmp = seq[i]
		j = i
		while j > 0 and seq[j-1] > tmp:
			seq[j] = seq[j-1]
			j -= 1
		seq[j] = tmp
        
def Insertsort(seq):
	length = len(seq)
	for i in range(1,length):
		tmp = seq[i]
		for j in range(i,0,-1):
			if seq[j-1] > tmp:
				seq[j] = seq[j-1]
			else:
				j=j+1
				break
		seq[j-1] = tmp	
        
def shellsort(seq):
	n = len(seq)
	inc=0
	while inc < n//3:
		inc = inc*3+1
	while inc:
		for i in range(inc,n):
			tmp = seq[i]
			j=i
			while j > 0 and seq[j-inc] > tmp:
				seq[j] = seq[j-inc]
				j -= inc
			seq[j] = tmp
		inc //= 3
        
def ShellSort(seq):
	length = len(seq)
	inc=0
	while inc < length/3:
		inc=inc*3+1
	print inc
	while inc:
		for i in range(inc,length):
			tmp=seq[i]
			for j in range(i,0,-inc):
				if seq[j-inc] > tmp:
					seq[j] = seq[j-inc]
				else:
					j+=inc
					break
			seq[j-inc] = tmp
		inc//=3
        
def merge_sort(seq):
    n = len(seq)
    if n <=1:
        return seq
    mid = n//2
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    def merge(left,right):
        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        while left:
            merged.append(left.pop(0))
        while right:
            merged.append(right.pop(0))
        return merged
    return merge(left,right)
    
        
def mergesort(seq):
	n = len(seq)
	if n > 1:
		mid = n//2
		left = seq[:mid]
		right = seq[mid:]
		mergesort(left)
		mergesort(right)
		def merge(left,right):
			l = len(left)
			r = len(right)
			print(left,'**',right)
			i = 0
			j = 0
			k = 0
			while i < l and j < r:
				if left[i] < right[j]:
					seq[k] = left[i]
					i += 1
				else:
					seq[k] = right[j]
					j+= 1
				k += 1
			while i < l:
				seq[k] = left[i]
				i += 1
				k += 1
			while j < r:
				seq[k] = right[j]
				j += 1
				k += 1
		merge(left,right)
		print(seq)
		
		
def mergesort(seq):
	n = len(seq)
	count = [0]
	if n > 1:
		mid = n//2
		left = seq[:mid]
		right = seq[mid:]
		count[0] += mergesort(left)
		count[0] += mergesort(right)
		def merge(left,right):
			l = len(left)
			r = len(right)
			i = 0
			j = 0
			k = 0
			while i < l and j < r:
				if left[i] <= right[j]:
					seq[k] = left[i]
					i += 1
				else:
					seq[k] = right[j]
					j+= 1
					count[0] += l-i
				k += 1
			while i < l:
				seq[k] = left[i]
				i += 1
				k += 1
			while j < r:
				seq[k] = right[j]
				j += 1
				k += 1
		merge(left,right)
	return count[0]

def MergeSort(seq):
	length = len(seq)
	if length <= 1:
		return seq
	mid = (length/2)
	left = MergeSort(seq[:mid])
	right = MergeSort(seq[mid:])
	#print "left right ",mid
	return merge(left,right)

def merge(left,right):
	result=[]
	i,j = 0,0
	lenleft = len(left)
	lenright = len(right)
	while i < lenleft and j < lenright:
		if left[i] <= right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	result+=left[i:]
	result+=right[j:]
	#print result
	return result    

def iter_mergersort(seq):
    q = []
    for i in range(seq):
        q.append([i])
    while len(q)>1:
        q.append(merge(q.pop(0),q.pop(0)))
    return q.pop(0)


        
        
def qsort(seq):
	def qsort_helper(seq,first,last):
		def partition(seq,first,last):
			pivot_value = seq[first]
			left = first+1
			right = last
			done = False
			while not done:
				while left <= right and seq[left] < pivot_value:
					left += 1
				while right >= left and seq[right] >= pivot_value:
					right -= 1
				if right < left:
					done = True
				else:
					seq[left], seq[right] = seq[right],seq[left]
					left += 1
					right -= 1
			seq[first],seq[right] = seq[right],seq[first]
			return right
		if first < last:
			split_point = partition(seq,first,last)
			qsort_helper(seq,first,split_point-1)
			qsort_helper(seq,split_point+1,last)
	qsort_helper(seq,0,len(seq)-1)

def select_i_less(seq,i):
	def select_i_less_helper(seq,first,last,i):
		def partition(seq,first,last):
			pivot_value = seq[first]
			left = first+1
			right = last
			done = False
			while not done:
				while left <= right and seq[left] < pivot_value:
					left += 1
				while right >= left and seq[right] >= pivot_value:
					right -= 1
				if right < left:
					done = True
				else:
					seq[left], seq[right] = seq[right],seq[left]
					left += 1
					right -= 1
			seq[first],seq[right] = seq[right],seq[first]
			return right
		if first < last:
			split_point = partition(seq,first,last)
			print(split_point,i,seq[first:split_point],seq[split_point:split_point+1],seq[split_point+1:last+1])
			if split_point == i:
				return seq[split_point]
			elif split_point > i:
				return select_i_less_helper(seq,first,split_point-1,i)
			else:
				return select_i_less_helper(seq,split_point+1,last,i)
		elif first == last:
			return seq[first]
	if 0 < i <= len(seq):
		return select_i_less_helper(seq,0,len(seq)-1,i-1)
	return -1

#不是原地    
def qsort(seq):
	if seq==[]:
		return []
	else:
		pivot = seq[0]
		lesser = qsort([x for x in seq[1:] if x<pivot])
		greater = qsort([x for x in seq[1:] if x>=pivot])
		return lesser+[pivot]+greater
		
		
		

			


			
def k_merge(iterables):
	h=[]
	for itnum,it in enumerate(map(iter,iterables)):
		try:
			h.append([it.next(),itnum,it.next])
		except StopIteration:
			pass
	heapq.heapify(h)
	while len(h) > 1 :
		try:
			while 1:
				v,itnum,_next = s = h[0]
				yield v
				s[0] = _next()
				heapq.heapreplace(h,s)
		except StopIteration:
			heapq.heappop(h)
	if h:
		v,itnum,_next = h[0]
		yield v
		for v in _next.__self__:
			yield v

def k_merge1(iterables):
	h=[]
	for itnum,it in enumerate(map(iter,iterables)):
		try:
			h.append([it.next(),itnum,it.next])
		except StopIteration:
			pass
	heapq.heapify(h)
	while 1:
		try:
			while 1:
				v,itnum,_next = s = h[0]
				yield v
				s[0] = _next()
				heapq.heapreplace(h,s)
		except StopIteration:
			heapq.heappop(h)
		except IndexError:
			return
					
if __name__=='__main__':
	seq=sample(xrange(100000),10)
	length = len(seq)
    seqe = list(seq)
	start = time()
	seqf=MergeSort(seqe)
	end = time()
	print "MergeSort %f" % (end-start)
	print seqf == seqa
	print seq == seqf
	
	
def test():
	x =k_merge1([
			[1,3,5,7], 
			[0,2,4,8], 
			[5,10,15,20], 
			[], 
			[25]
		  ])
	for i in range(12):
		x.next()
	x.next()
	x.next()

def testsort():
	#seq = range(1000)
	seq=sample(xrange(1000),10)
	seq = seq*2
	length = len(seq)
	seqa = list(seq)
	start = time()
	BubbleSort(seqa)
	end = time()
	print "BubbleSort %f" % (end-start)
	if length <= 10:
		print seq
		print seqa
	seqb = list(seq)
	start = time()
	BubbleSort1(seqb)
	end = time()
	print "BubbleSort1 %f" % (end-start)
	seqc = list(seq)
	start = time()
	BubbleSort1(seqc)
	end = time()
	print "BubbleSort2 %f" % (end-start)
	seqd = list(seq)
	start = time()
	SelectSort(seqd)
	end = time()
	print "SelectSort %f" % (end-start)
	if length <= 10:
		print seqd
	print seqa == seqd
	seqe = list(seq)
	start = time()
	SelectSort1(seqe)
	end = time()
	print "SelectSort %f" % (end-start)
	print seqa == seqe
	seqe = list(seq)
	start = time()
	ShellSort(seqe)
	end = time()
	print "ShellSort %f" % (end-start)
	print seqa == seqe
	print seq == seqe
	seqe = list(seq)
	start = time()
	seqf=MergeSort(seqe)
	end = time()
	print "MergeSort %f" % (end-start)
	print seqf == seqa
	print seq == seqf
	seqe = list(seq)
	start = time()
	seqf=qsort(seqe)
	end = time()
	print "qsort %f" % (end-start)	
	print seqa == seqf
	print seq == seqf
		
	