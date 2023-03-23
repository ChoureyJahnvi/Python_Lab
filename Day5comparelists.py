list1 = []
n = int(input("enter number of elements of list1:")) # input from user in l1
for i in range (0,n):
    l1 = input()
    list1.append(l1) # appending items in list1
print("list 1:",list1)

list2 = []
p = int(input("enter number of elements in list 2: ")) # input from user in l1
for j in range (0,p):
    l2 = input()
    list2.append(l2) # appending items in list2
print("list 2:",list2)

for k in list2:  # for items in list2
    if k in list1:  # if the items are in list1
        declare = "Equal"
    else:
        declare = "Not Equal"

print(declare)

