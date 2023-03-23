def add(a,b): # defining function for sum
    s = a+b
    return s
def subtract(a,b) :  # defining function for difference
    d=b-a
    return d
def multiplication (a,b) :  # defining function for product
    p=a*b
    return p
def division(a,b) :  # # defining function for quotient
    q=a/b
    return q

# providing users choice for choosing operation
print("enter choice"
      "1:add",
      "2:subtract",
      "3:multiplication",
      "4:division")

# taking value of a and b
a = int(input("enter a:"))
b = int(input("enter b:"))
choice = (input("enter operation:1,2,3,4 :")) # choosing operation
# conditions
if choice=='1':
    print("sum is", add(a,b))
elif choice == '2':
    print("difference  is", subtract(a, b))
elif choice =='3':
    print("product is ", multiplication(a,b))
elif  choice=='4':
    print ("quotient is", division(a,b))
else:
    print("invalid choice")
