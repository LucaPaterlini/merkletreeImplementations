# List Of Implementations
 -  A.py my implementation (it could be wrong its just my understanding) https://github.com/LucaPaterlini/merkletreeImplementations
 -  B.py taken from the merkletools pip package https://github.com/Tierion/pymerkletools/issues
 -  C.py Evan Kozliner implentation https://github.com/evankozliner/merkle-tree
 -  D.py tutorial example https://github.com/JaeDukSeo/Simple-Merkle-Tree-in-Python
 -  E.py lib package merkletree https://github.com/jvsteiner/merkletree
 
 # Question
 
 Assuming we have to be able to redo the same operation in order to allways get the same root corresponding to the same
 array in input with the element in the same order there are no more then 1 valid solution to be a merkle tree that can
 tested for each hashing function. Then, witch of those is the right one?
 
 As well if we consider the standard the bitcoin implentation, its written by its author that it have a potential flow due to the 
 wrong handling of the odd lists 
 https://github.com/bitcoin/bitcoin/blob/bccb4d29a8080bf1ecda1fc235415a11d903a680/src/consensus/merkle.cpp 

 
 P.S. I am in the comptia (https://www.comptia.org/) council regarding blokchain and my first tought was to currectly address 
 and define what a merkle tree is and how to calculate its root
