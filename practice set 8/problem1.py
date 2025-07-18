# write a program to find greatest of 3 numbers using functions

def great():
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    c=int(input("Enter number: "))
    greatest=a
    if(b>greatest):
        greatest=b
    if(c>greatest):
        greatest=c
    print(greatest)

great()