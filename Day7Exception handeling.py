#exception handeling in python
try: # need to write where error may occur
    n= int(input("Enter any number for n"))
    print("numerator=",n)
    d=int(input("Enter any number for d"))
    print("denominator=",d)
    result = n/d
    print(result)

except ZeroDivisionError : #this error will happen and print the sentence instead of that error
    print("error: d can not be 0")

else : # if error does not occur it will print the else part
    r=1/n
    print(r)