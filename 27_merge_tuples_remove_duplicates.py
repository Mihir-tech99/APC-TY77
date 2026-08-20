# Program 27: Merge two tuples and remove duplicate elements
tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

merged = tuple(dict.fromkeys(tuple1 + tuple2))

print("Merged tuple without duplicates:", merged)
