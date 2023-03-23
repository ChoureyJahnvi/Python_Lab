# creating tuples
t1 = (1, 2, 3)
print(t1)

# tuple with different data types
t2 = ("jahnvi", 101, 2003, 20.6)
print(t2)

# length of tuple
print("length of tuple",len(t2))

# nested tuple list
l=[t2,3,7,89,54]
# printing tuple in list
print(l)

# converting tuple to list
l2 = list(t2)
print(t2)
# changing value of element in list
l2[3]= "Chourey"
print(l2)

t=((1,"jahnvi", 20.6, 2003))
print (t)
# Functions in tuple:
print("Length of tuple", len(t))  # length of tuple
print("Backward indexing : ", t[-1])  # Backward indexing getting element
print("Forward indexing : ", t[0])  # Forward indexing getting element
print("Slicing using forward indexing", t[1:2])  # slicing in tuple



