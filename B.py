from merkletools import *

mt = MerkleTools()

list_data = ["a","b","c"]


mt.add_leaf(list_data, True)
mt.make_tree()

print "root:", mt.get_merkle_root()