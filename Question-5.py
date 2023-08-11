# Write a python program to print all key names in the dictionary, one by one

print()
d1 =  {'Name': 'Sandeep', 'Age': '21', 'Gender': 'Male', 'Caste': 'General', 'Odour': 'Fragnant'}
d2 = {}

for i in d1:
    key = i
    data = d1[i]
    d2[key] = data
    print(d2)

print()
