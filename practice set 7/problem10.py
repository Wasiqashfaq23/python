# write a table for n using for loop in reverse


f=10
n=int(input("Enter the number: "))
for i in range(1,11):
    product=n*f
    print(f"{n} x {f} =",product)
    f-=1