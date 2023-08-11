# Write a python program to create a dictionary that contains three dictionary (nested)

print()
d1 = {}
d2 = {}
d3 = {}

key1 = input("Enter the key for first dictionary: ")
data1 = input("Enter the data: ")
d1[key1] = data1

key2 = input("Enter the key for second dictionary: ")
d2[key2] = d1

key3 = input("Enter the key for third dictionary: ")
d3[key3] = d2

dict_main = {}
key_main = input("Enter the key for main dictionary: ")
dict_main[key_main] = d3

print(dict_main)
print()