marks={
    "Wasiq":100,
    "Saqaf":87,
    "Usama":23,
    0:"Harry"
}

print(marks.items())

print(marks.keys())  #keys are on LHS

print(marks.values())  # values are on RHS

marks.update({"Wasiq":99 , "Hello":89})  # if key value pair not exist it adds  
print(marks)

print(marks.get("Wasiq"))
print(marks["Wasiq"])


print(marks.get("Wasiq1"))
print(marks["Wasiq1"])  #gives error

# in get methods if we not fond the key we get none while in simple method we get error