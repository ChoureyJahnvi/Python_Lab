# Creating Lists
l1 = [1,2,3,4,5,6,7,8]
type(l1) # printing list
print(l1)

# length of list
print("length of list is",len(l1))

# diff btw list nd tuple is can manipulate  more items in lists(lists are mutable but in tuple we cannot add

l2 = ["a",10.6,4]
print(l2)

# appending(adding at last) element
l2.append(34)
print(l2)

# removing element
l2.remove("a")
print(l2)

# poping out last element
l2.pop()
print(l2)


t=list((4,2,7,1,5,6))
print(t)
# sorting list using sort function
t.sort()
print(t)

#set remove duplicates and will arrange in ascending order
t=set((1,23,4))
print(t)

t1 = set((1,3,5,2,6,3,4,5,6))
print(t1)

t2 = set({2,3,6,8,3,4,2})
print(t2)