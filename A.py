#THE PROPOSED test

#Given an array of byte objects generate a Merkle root hash using the SHA256 algorithm.
# Time: 15 minutes Input: ["a", "b", "c", "d"] Output: 14ede5e8e97ad9372327728f5099b95604a39593cac3bd38a343ad76205213e7
# Input: ["a", "b", "c"] Output: e76328b6ca10676c686a0d534e8222ad8da04fdfe14c6f6ff67d08cbbd24c605


#The actual implentation

import hashlib

def merkletreeroot(arr):
    # initialize
    la = len(arr)
    for i in xrange(la):
        arr[i] = hashlib.sha256(arr[i]).hexdigest()
    #build
    while len(arr) != 1:
        tmp = []
        la = len(arr)
        for i in xrange(0, la, 2):
            left=arr[i]
            rigth = arr[i+1] if la != i+1 else ""
            tmp.append(hashlib.sha256(left+rigth).hexdigest())

        arr = tmp
    return arr[0]

print merkletreeroot(["a", "b", "c","d"])
print "58c89d709329eb37285837b042ab6ff72c7c8f74de0446b091b6a0131c102cfd"

print merkletreeroot(["a", "b", "c"])
print "35172c364a0d06a3ddbd3869ff682dd0395fad299787cda9c74cea0a14d8dc41"


