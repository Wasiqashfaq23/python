# print a pattern 
'''
***
**
*
for n=3
'''

def pattern():
    n=int(input("Enter the number: "))
    k=n
    for i in range (1,n+1):
        print("*"*k)
        k-=1

pattern()


# or we can do it like

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

n=int(input("Enter the number: "))
pattern(n)