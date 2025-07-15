# String is a datatype in python
# string is immutable
# length in a string is the total no characters in a string 
# can find it by

name="wasiq"
print(len(name))

# we can slice a sring by

# variable=thestringvariable[slice-start  :  start-end]

nameshort=name[1:4]  # start allway from index 1 all way to 4   //4 will not be included
print(nameshort)


# or we can get a characer by 
# variable = string variable [1]


character=name[0]  #character at 0 indent
print(character)



# if it is written like 

print(name[:4])   # it will be sam eas [0:4]
print(name[1:])   # it will be same as [1:5]


# skip values in slicing 

word="0123456789"
withskippedword=word[1:7:3]  #start from 1 end at 7   [123456]  skip value is 3 [1 skip 3  then print 4th then again 3]
#answer wil be 14 start from 1 end at 7 and skip 3  value print 4th  value
print(withskippedword)
