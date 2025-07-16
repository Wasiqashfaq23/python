# empty dict allow 4 friend to enter their favourite language as value and keys as their names , names are unique
# what if name is same
# if name are same later value is updated

dict={}

a=input("Enter name: ")
b=input("Enter language: ")

dict.update({a:b})

a=input("Enter name: ")
b=input("Enter language: ")

dict.update({a:b})

a=input("Enter name: ")
b=input("Enter language: ")
dict.update({a:b})

a=input("Enter name: ")
b=input("Enter language: ")
dict.update({a:b})

print(dict)

