# Write a python program to access the items of a dictionary by referring to its key name.

print()
d1 =  {'Name': 'Sandeep', 'Age': '21', 'Gender': 'Male', 'Caste': 'General', 'Odour': 'Fragnant'}
print(d1.keys())

print()
key = input("Enter the key value from above: ")
print(key,":",d1[key])

print()