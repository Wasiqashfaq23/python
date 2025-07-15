a=input("Enter number 1:")
b=input("Enter number 2:")

print ("A is: " ,a)
print ("B is: " ,b)

print ("Sum is " , a+ b)   #the output here is the ab like if a is 1 b is 2
# then output is not 3 it is 12 
# because in input it is treating a and b as string here not int
# in short concatination



# we can write it like as below and we they will be treated as int


a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))

print ("A is: " ,a)
print ("B is: " ,b)

print ("Sum is " , a+ b) #here output will be 5