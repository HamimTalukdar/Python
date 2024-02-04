set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Union of sets
union_set = set1.union(set2)
print(union_set)  # {1, 2, 3, 4, 5, 6, 7}

# Intersection of sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # {3, 4, 5}

# Difference of sets
difference_set = set1.difference(set2)
print(difference_set)  # {1, 2}

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # {1, 2, 6, 7}
