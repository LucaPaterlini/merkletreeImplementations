
# IDEA 2
## This version A1 prepend the incremental byte that signal the level of
## the tree


import binascii
import hashlib

def merkletreeroot(arr):
    # initialize
    la = len(arr)
    level = 0x00
    for i in xrange(la):
        v = arr[i].encode('utf-8')
        v = hashlib.sha256(bytes(level)+v).hexdigest()
        v = bytearray.fromhex(v)
        arr[i] = v
    #build
    while len(arr) != 1:
        level+=1
        tmp = []
        la = len(arr)
        for i in xrange(0, la, 2):
            left=arr[i]
            rigth = arr[i+1] if la != i+1 else b''
            v = hashlib.sha256(bytes(level)+left+rigth).digest()
            tmp.append(v)

        arr = tmp
    return binascii.hexlify(arr[0])

print merkletreeroot(["a", "b", "c","d"])
print "14ede5e8e97ad9372327728f5099b95604a39593cac3bd38a343ad76205213e7"

print merkletreeroot(["a", "b", "c"])
print "e76328b6ca10676c686a0d534e8222ad8da04fdfe14c6f6ff67d08cbbd24c605"


