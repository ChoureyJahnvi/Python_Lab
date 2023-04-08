f1 = open("tests.txt",'r') #reading a file
read = f1.read() #using read command
print(read)

#reading using read line
f1 = open("tests.txt",'r') #reading a file
print(f1.readline())# will read only first line

#reading using read lines
f1 = open("tests.txt",'r')
print(f1.readlines())# will read whole as dictionary

#writing a file
#f1 = open("tests.txt",'w')# opening file
#write = f1.write('hi its me')# passing argument
#print(write)# its will print the number of characters in arguments and willupdate the textdoc



