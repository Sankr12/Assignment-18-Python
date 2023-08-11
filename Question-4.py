# Write a python program to change the value of a specific item by referring to its key name. 

print()
d1 =  {'Name': 'Sandeep', 'Age': '21', 'Gender': 'Male', 'Caste': 'General', 'Odour': 'Fragnant'}
print(d1.keys())

print()
key = input("Enter the key value from above: ")

print()
value = input("Enter the value you want to change: ")

d1[key] = value

print(d1)
print()