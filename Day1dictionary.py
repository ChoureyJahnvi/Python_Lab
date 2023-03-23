# Dictionary has key and value key written in ""and its value is given using :
# Dictionary
t= {1:"apple","b":"mango",3:"jahnvi"}
# Printing Dictionary
print(t)

# adding value to dictionary
t["add"] = "ICB"
# Printing Dictionary
print(t)

# removing value to dictionary
t.pop("add")
# Printing Dictionary
print(t)

# updating using update function
t.update({"b": "updated value"})
# Printing Dictionary
print(t)

# only inmutable things can be passed as key in dictionary i.e list cannot be used as key for dictionary
#fun
t2 = dict({"a":[1,2,3,4,5,6,7,8,]})
print(t2)

