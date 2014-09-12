__author__ = 'Administrator'

from hashlib import md5
class HashRing(object):
    def __init__(self,nodes=None,replicas=3):
        self.ring = dict()
        self.replicas = replicas
        self._sorted_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    def gen_key(self,key):
        m = md5.new()
        m.update(key)
        return long(m.hexdigest(),16)

    def add_node(self,node):
        for i in xrange(0,self.replicas):
            key = self.gen_key("%s:%s" % (node,i))
            self.ring[key] = node
            self._sorted_keys.append(key)

        self._sorted_keys.sort()

    def remove_node(self,node):
        for i in xrange(0,self.replicas):
            key = self.gen_key("%s:%s" % (node,i))
            del self.ring[key]
            self._sorted_keys.remove(key)

    def get_node(self,string_key):
        return self.get_node_pos(string_key)[0]

    def get_node_pos(self,string_key):
        if not self.ring:
            return None, None
        key = self.gen_key(string_key)
        nodes = self._sorted_keys
        for i in xrange(0, len(nodes)):
            node = nodes[i]
            if key <= node:
                return self.ring[node],i

        return self.ring[nodes[0]],0
