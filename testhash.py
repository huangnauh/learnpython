from hashlib import md5
from struct import unpack_from
from time import time
from bisect import bisect_left
def test1():
	start = time()
	Node_Count = 100
	New_Node_count = 101
	Data_Id_Count = 10000000
	moved_ids = 0
	node_counts = [0] * Node_Count
	new_node_counts = [0] * New_Node_count
	

	for data_id in xrange(Data_Id_Count):
		#hsh = long(md5(str(data_id)).hexdigest(),16)
		hsh = unpack_from('>I',md5(str(data_id)).digest())[0]
		node_id = hsh % Node_Count
		new_node_id = hsh % New_Node_count
		if node_id != new_node_id:
			moved_ids += 1
		node_counts[node_id] += 1
		new_node_counts[new_node_id] += 1
		
	percent_moved = 100.0 * moved_ids / Data_Id_Count
	print '%d ids moved, %.02f%%' % (moved_ids, percent_moved)
	duration = time()-start
	print "time:",duration
	max_count = max(node_counts)
	desired_count = Data_Id_Count / Node_Count
	over = 100.0 * (max_count - desired_count) / desired_count
	print '%d: Most data ids on old node, %.02f%% over' % (max_count, over)
	min_count = min(node_counts)
	under = 100.0 * (desired_count - min_count) / desired_count
	print '%d: Least data ids on old node, %.02f%% under' % (min_count, under)

	max_count = max(new_node_counts)
	desired_count = Data_Id_Count / New_Node_count
	over = 100.0 * (max_count - desired_count) / desired_count
	print '%d: Most data ids on new node, %.02f%% over' % (max_count, over)
	min_count = min(new_node_counts)
	under = 100.0 * (desired_count - min_count) / desired_count
	print '%d: Least data ids on new node, %.02f%% under' % (min_count, under)
def test2():
	start = time()
	NODE_COUNT = 100
	NEW_NODE_COUNT = 101
	DATA_ID_COUNT = 10000000
	moved_ids = 0
	node_range_starts = []
	for node_id in xrange(NODE_COUNT):
		node_range_starts.append(DATA_ID_COUNT / NODE_COUNT * node_id)
	new_node_range_starts = []
	for new_node_id in xrange(NEW_NODE_COUNT):  
		new_node_range_starts.append(DATA_ID_COUNT / NEW_NODE_COUNT * new_node_id) 
	node_counts = [0] * NODE_COUNT
	new_node_counts = [0] * NEW_NODE_COUNT
	for data_id in xrange(DATA_ID_COUNT):  
		hsh = unpack_from('>I', md5(str(data_id)).digest())[0]  
		node_id = bisect_left(node_range_starts, hsh % DATA_ID_COUNT) % NODE_COUNT
		new_node_id = bisect_left(new_node_range_starts,hsh % DATA_ID_COUNT) % NEW_NODE_COUNT
		if node_id != new_node_id:
			moved_ids +=1
		node_counts[node_id] += 1
		new_node_counts[new_node_id] += 1
	percent_moved = 100.0 * moved_ids / DATA_ID_COUNT
	print '%d ids moved, %.02f%%' % (moved_ids, percent_moved)
	duration = time()-start
	print "time:",duration
	
	max_count = max(node_counts)
	desired_count = DATA_ID_COUNT / NODE_COUNT
	over = 100.0 * (max_count - desired_count) / desired_count
	print '%d: Most data ids on old node, %.02f%% over' % (max_count, over)
	min_count = min(node_counts)
	under = 100.0 * (desired_count - min_count) / desired_count
	print '%d: Least data ids on old node, %.02f%% under' % (min_count, under)

	max_count = max(new_node_counts)
	desired_count = DATA_ID_COUNT / NEW_NODE_COUNT
	over = 100.0 * (max_count - desired_count) / desired_count
	print '%d: Most data ids on new node, %.02f%% over' % (max_count, over)
	min_count = min(new_node_counts)
	under = 100.0 * (desired_count - min_count) / desired_count
	print '%d: Least data ids on new node, %.02f%% under' % (min_count, under)
	

def test3():
	start = time()
	NODE_COUNT = 100
	NEW_NODE_COUNT = 101
	DATA_ID_COUNT = 10000000
	VNODE_COUNT = 1000
	moved_ids = 0
	vnode_range_starts = []
	vnode2node = []
	for vnode_id in xrange(VNODE_COUNT):  
		vnode_range_starts.append(DATA_ID_COUNT / VNODE_COUNT * vnode_id)  
		vnode2node.append(vnode_id % NODE_COUNT)
	new_vnode2node = list(vnode2node)
	new_node_id = NODE_COUNT
	vnodes_to_reassign = VNODE_COUNT / NEW_NODE_COUNT
	while vnodes_to_reassign > 0:
		for node_to_take_from in xrange(NODE_COUNT):  
			for vnode_id, node_id in enumerate(new_vnode2node):  
				if node_id == node_to_take_from:
					new_vnode2node[vnode_id] = new_node_id
					vnodes_to_reassign -= 1
					break
			if vnodes_to_reassign <= 0: 
				break
	node_counts = [0] * NODE_COUNT
	new_node_counts = [0] * NEW_NODE_COUNT
	for data_id in xrange(DATA_ID_COUNT):  
		hsh = unpack_from('>I', md5(str(data_id)).digest())[0]  
		vnode_id = bisect_left(vnode_range_starts, hsh % DATA_ID_COUNT) % VNODE_COUNT
		node_id = vnode2node[vnode_id] 
		new_node_id = new_vnode2node[vnode_id]
		if node_id != new_node_id:
			moved_ids +=1
		node_counts[node_id] += 1
		new_node_counts[new_node_id] += 1
	percent_moved = 100.0 * moved_ids / DATA_ID_COUNT
	print '%d ids moved, %.02f%%' % (moved_ids, percent_moved)
	duration = time()-start
	print "time:",duration
	
	max_count = max(node_counts)
	desired_count = DATA_ID_COUNT / NODE_COUNT
	over = 100.0 * (max_count - desired_count) / desired_count
	print '%d: Most data ids on old node, %.02f%% over' % (max_count, over)
	min_count = min(node_counts)
	under = 100.0 * (desired_count - min_count) / desired_count
	print '%d: Least data ids on old node, %.02f%% under' % (min_count, under)

	max_count = max(new_node_counts)
	desired_count = DATA_ID_COUNT / NEW_NODE_COUNT
	over = 100.0 * (max_count - desired_count) / desired_count
	print '%d: Most data ids on new node, %.02f%% over' % (max_count, over)
	min_count = min(new_node_counts)
	under = 100.0 * (desired_count - min_count) / desired_count
	print '%d: Least data ids on new node, %.02f%% under' % (min_count, under)
	
test1()
test2()
test3()