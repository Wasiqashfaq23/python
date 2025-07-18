# a function which calls itself is recursion

''' 
factorial(1)= 1
factorial(2)= 2 x 1
factorial(3)= 3 x 2 x 1
factorial(4)= 4 x 3 x 2 x 1
factorial(5)= 5 x 4 x 3 x 2 x 1

factorial(n)= n x n-1 x ...... x 3 x 2 x 1

factorial(n)= n * factrial(n-1)

'''


def factorial(n):
    if (n==1 or n==0):
        return 1
    return n * factorial (n-1)


n=int(input("Enter your number: "))
print(f"Factorial of {n} is {factorial(n)}")

# be careful while using factorial 