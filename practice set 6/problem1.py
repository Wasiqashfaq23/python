# write a program to find the greatest of four numbers 

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
d=int(input("Enter 4th number: "))

if(a>b and a>c and a>d):
    print(f"Greatest number is: {a}")
elif(b>a and b>c and b>d):
    print(f"Greatest number is: {b}")
elif(c>a and c>b and c>d):
    print(f"Greatest number is: {c}")
elif(d>a and d>b and d>c):
    print(f"Greatest number is: {d}")

