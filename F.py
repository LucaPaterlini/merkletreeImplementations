from pymerkle import *            # Import merkle_tree, validate_proof
                                  # and proof_validator

tree = merkle_tree(hash_type='sha256', encoding='utf-8', security=True)

for c in ["a", "b", "c", "d"]:
    tree.update(c)

print(tree.root_hash())
print("14ede5e8e97ad9372327728f5099b95604a39593cac3bd38a343ad76205213e7")
tree = merkle_tree(hash_type='sha256', encoding='utf-8', security=True)


for c in ["a", "b", "c"]:
    tree.update(c)

print(tree.root_hash())
print("e76328b6ca10676c686a0d534e8222ad8da04fdfe14c6f6ff67d08cbbd24c605")