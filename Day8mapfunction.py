#map function will map the argument paseed with the list provided and will present you with a new list with the results
l= [3,4,5,6,7,8,9] #defining list

def multiply (l) : #passing argument in function
    return l*2

#apply function to list
newlist = map(multiply,l)

#converting answers to list
newlist = list(newlist)
print(newlist)

