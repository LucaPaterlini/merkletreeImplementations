# List Of Implementations (Python)
 -  A.py my implementation (it could be wrong its just my understanding) https://github.com/LucaPaterlini/merkletreeImplementations
 -  B.py taken from the merkletools pip package https://github.com/Tierion/pymerkletools/issues
 -  C.py Evan Kozliner implentation https://github.com/evankozliner/merkle-tree
 -  D.py tutorial example https://github.com/JaeDukSeo/Simple-Merkle-Tree-in-Python
 -  E.py lib package merkletree https://github.com/jvsteiner/merkletree
 -  F.py lib package pymerkle(python 3) https://github.com/FoteinosMearg/pymerkle
 
 N.B. none of those different implentations returns the same output on the same input
 
 # Question
 
 Assuming we have to be able to redo the same operation in order to allways get the same root corresponding to the same
 array in input with the element in the same order there are no more then 1 valid solution to be a merkle tree that can
 tested for each hashing function. Then, witch of those is the right one?
 
 As well if we consider the standard the bitcoin implentation, its written by its author that it have a potential flow due to the 
 wrong handling of the odd lists 
 https://github.com/bitcoin/bitcoin/blob/bccb4d29a8080bf1ecda1fc235415a11d903a680/src/consensus/merkle.cpp 
 
 A1.py shows this inmplentation instead
 
  # Question 2
 
 Isn't it better to avoid the Second preimage attack as proposed on wiki https://en.wikipedia.org/wiki/Merkle_tree
 by adding a byte at the begin of each level of hashing to certify the dept of the structure?(this way the implicit limit of 
 the list is 2**(2**8) = 115792089237316195423570985008687907853269984665640564039457584007913129639936L (still a big number)
 
 P.S. I am in the comptia (https://www.comptia.org/) council regarding blokchain and my first tought was to currectly address 
 and define what a merkle tree is and how to calculate its root

#Answers

Feel free to open inssues with your answers on this github repo.
Tk in advance for your feedback, LP