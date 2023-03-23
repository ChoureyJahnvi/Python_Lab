# Filter function filters sequence( sets, lists, tuples etc) acc to the function defined
# Function will check for the element in the sequence ..
# SYNTAX: filter(function, sequence)

def fun(check) : # defining function
    l1=[0,2,4,6,8]
    if (check in l1 ): # command to check the provided element
        return true
    else:
        return false

list1 = [1,2,3,4,5,6,7,8,9,0] # sequence
lol= filter(fun,list1)
print ("The updated list is:")


# for checking even number in list
def fun(n):
    if n % 2 == 0:
        return True
    else:
        return False


L = [1, 4, 5, 3, 6, 9]
a = filter(fun, L)  # calling function
for n in a:
    print(n) # printing filtered element
