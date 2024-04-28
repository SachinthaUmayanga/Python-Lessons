x = 5
y = 20
z = 100

#-------------First method-----------
if(x>y):
    print("x is bigger")
elif(y>z):
    print("y is bigger")
else:
    print("z is bigger")


#=------------seconf method-------------
max_value = max(x,y,z)
print("the highest value: ",max_value)

#---------Find the minimum value-------------
min_value = min(x,y,z)
print("Lowest value: ",min_value)


