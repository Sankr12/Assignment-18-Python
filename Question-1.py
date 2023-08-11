# Write a python program to create and print a dictionary which stores your information. (name, age, gender ....) 

print()
num = int(input("Enter the number of data you want to input: "))
d1 = {}

for i in range(num):
    key = input("Enter the key: ") 
    data = input("Enter the data: ")
    d1[key] = data

print("Dictionary: ",d1)    
print()