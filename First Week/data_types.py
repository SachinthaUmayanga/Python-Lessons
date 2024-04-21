x="Python{}"
y="\nHello world---"
z="""\nHEllo world..."""

#check the data type
#print(type(x),x)

# print(x,y,z)

#print the first letter of the x
# print(x[0])

#print the second letter of the last side
# print(x[-2])

a=0
# print(type(a))

#to pass the value use the {} and print code like the following
# print(x.format(a))

# 
# print (x+y+str(a))


# print(f"Sachintha {x}")

b=0.0
# print(type(b))

# print ("Configure git")

#List
l1= [1,2,3,"Sachintha",0.0]
# print(l1[3])

#print a range of the list
# print(l1[0:4])

#find the length of the list
# print(len(l1))

#tuple
tuple = (1,2,3,4,5)
# print(tuple)

#boolean
# is_created = False
# is_false = True
# print(is_created, type(is_created))
# if 2>0:
#     is_created = True
# print(is_created)

#Set (remove the duplicate values from list)
set1 = set([1,2,'geeks',4,'geeks'])
# print(set1)

#dictionary
dict = {}
dict1 = {
    "Name": "Sachintha",
    "Age": 25,
    "Mobile": '0764452125',
}
dict2 = {
    "Name": "Umayanga",
    "Age": 25,
    "Mobile": '0762452133',
}
print(dict1['Mobile'])
list = []
## append dictionary to a list
list.append(dict1)
list.append(dict2)
# print(list)

import pandas as pd
df = pd.DataFrame(list)
print(df.head())
print(type(df))