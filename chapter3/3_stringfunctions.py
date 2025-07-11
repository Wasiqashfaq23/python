# first function is len
name="wasiq"
print(len(name))

# endswith function tells the ending values 
# like

print(name.endswith("siq"))

# also we have starts with

print(name.startswith("was"))

# also we can capitalize the first string

print(name.capitalize())


# title()  makes each first letter of the word capital 

title="Pirates of the carrabian"
print(title.title())


# find()  tells the indent where the first letter of finding word is located 
# in "Hello world"  we are finding "world"  w of world is at 6th indent so 
# output will be 6

string="hello world"
print(string.find("world"))


# also we can replace the word in a string 
# string.replace("oldword" , "newword")
# it replaces all occurences
new_word=(string.replace("hello" , "good bye"))
print(new_word)


str="wasiq is a good good boy"
new_str=str.replace("good", "bad")
print(new_str)
