# Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries

print()
d1 = {51:"Sandeep"}
d2 = {33:"Manish"}
d3 = {71:"Vikas"}

dict_main = {}
for i in range(3):
    if i<1:
        key = input("Enter the key: ")
        dict_main[key] = d1
    elif i==1:
        key = input("Enter the key: ")
        dict_main[key] = d2
    else:
        key = input("Enter the key: ")
        dict_main[key] = d3

print(dict_main)
print()