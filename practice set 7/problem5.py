# write a program to add n natural number using while 

n=int(input("Enter your number: "))

i=1
sum=0
while(i<n+1):
    sum+=i
    i+=1
print(sum)