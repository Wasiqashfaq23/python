# here both of the if statements work independently
a=int(input("Enter Your age: "))

# if statement 1
if(a%2==0):
    print("Age is even")
# end of if statement 1



# if statement 2
if(a>=18):
    print("You can go out")
elif(a<0):
    print("You entered Invalid age")
elif(a==0):
    print("0 is not a valid age")
else:
    print("You cannot go out")
# end of if statement 2

# elif and else cant be alone they always require an if statement always