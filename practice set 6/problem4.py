# check wether a username has less than 10 character or not

name=input("Enter your name: ")
length=len(name)
if(length<10):
    print("Less than 10")
elif(length==10):
    print("Equal to 10")
else:
    print("Greater than 10")
