# write a recursive function to calculate sum of first n natural numbers


'''

1+2+3+4+5+.....n

sum(1)=1
sum(3)=1+2
sum(3)=1+2+3
sum(4)=1+2+3+4
sum(5)=1+2+3+4+5
# we have to apply a base condition to stop the recursion at some point

'''
def sum(n):
    if n==1:
        return 1
    return sum(n-1) + n



n=int(input("Enter the number: "))
print(sum(n))