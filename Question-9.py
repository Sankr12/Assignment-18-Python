# Write a python program to merge two dictionaries into one dictionary.

print()
dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}

print("Dictionary1:",dict1)
print("Dictionary2:",dict2)

print()
dict1.update(dict2)

print("Merged Dictionary:", dict1)
print()