# Write a python program to convert two lists into a dictionary in a way that item from
# list1 is the key and item from list2 is the value.

print()

list1 = [10, 20, 30]
list2 = ['apple', 'banana', 'orange']
d = {}

for i in range(3):
    d[list1[i]] = list2[i]

print(d)
print()