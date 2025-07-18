# write a function to print a multiplication table of given number

def table():
    no=int(input("Enter the number: "))
    for i in range(1,11):
        print(f"{no} * {i} is",no*i)
table()