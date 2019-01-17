from merkletools import *

mt = MerkleTools()

list_data = ["a","b","c","b"]


mt.add_leaf(list_data, True)
mt.make_tree()

print mt.get_merkle_root()
print "14ede5e8e97ad9372327728f5099b95604a39593cac3bd38a343ad76205213e7"

mt = MerkleTools()

list_data = ["a","b","c"]


mt.add_leaf(list_data, True)
mt.make_tree()

print mt.get_merkle_root()
print "e76328b6ca10676c686a0d534e8222ad8da04fdfe14c6f6ff67d08cbbd24c605"