# elif when we want to add multiple conditions

a=int(input("Enter Your age: "))

if(a>=18):
    print("You can go out")
elif(a<0):
    print("You entered Invalid age")
elif(a==0):
    print("0 is not a valid age")
else:
    print("You cannot go out")


