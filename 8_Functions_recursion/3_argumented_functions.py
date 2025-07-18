# functions with some arguments

def goodday(name,ending):
    print("Good day, "+ name)
    print(ending)


goodday("Wasiq","Thank you")
goodday("Saqaf","Thank you")
goodday("Wamiq","Thank you")
goodday("Usama","Thank you")
goodday("Hashir","Thanks")


# we can also return a value
def goodday(name,ending):
    print("Good day, "+ name)
    print(ending)
    return("Done")

a = goodday("Wasiq","Thank you")
print(a)