# empty dict allow 4 friend to enter their favourite language as value and keys as their names , names are unique
# what if value is same
# va,ues can be same inside of a DICT

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

