# Write a python program to get the key of the lowest value from the dictionary.
# sample_dict = {
#  'C': 92,
#  'Java': 66,
#  'Python': 85
# }

print()
sample_dict = {'C': 92, 'Java': 66, 'Python': 85}

min_value = min(sample_dict.values())
lowest_key = None

for key, value in sample_dict.items():
    if value == min_value:
        lowest_key = key
        break

if lowest_key is not None:
    print(f"The key with the lowest value is: {lowest_key}")
else:
    print("The dictionary is empty.")
print()