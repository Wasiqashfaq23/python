# check wether a number is prime or not

n=int(input("Enter your number: "))

for i in range (2,n):
    if(n%i==0):
        print("Number not prime.")
        break
else:
    print("Prime number")
