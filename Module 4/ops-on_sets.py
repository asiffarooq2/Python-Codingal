# Set Operations

def set_operations():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}

    print("Set 1:", set1)
    print("Set 2:", set2)

    print("Union:", set1.union(set2))
    print("Intersection:", set1.intersection(set2))
    print("Difference (Set1 - Set2):", set1.difference(set2))
    print("Symmetric Difference:", set1.symmetric_difference(set2))


set_operations()
