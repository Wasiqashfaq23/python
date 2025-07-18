# factorial of a given number

n=int(input("Enter your number: "))

product =1
for i in range(1 , n+1):
    product *= i
print(f"Factorial of {n} is {product}")