# Original https://github.com/jvsteiner/merkletree
from merkle import *

mt =MerkleTree(["a","b","c","d"])
mt.build()
print mt.root.val.encode('hex')
print "14ede5e8e97ad9372327728f5099b95604a39593cac3bd38a343ad76205213e7"

mt =MerkleTree(["a","b","c"])
mt.build()
print mt.root.val.encode('hex')
print "e76328b6ca10676c686a0d534e8222ad8da04fdfe14c6f6ff67d08cbbd24c605"

