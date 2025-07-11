# question 2 write a template letter by replace
#    Dear [name],
#    You are selected!
#    [Date]


letter= ''' \t    Dear <|Name|>,
            You are selected!
            <|Date|>  '''


print(letter.replace("<|Name|>","Wasiq").replace("<|Date|>","24,Sep,2028"))


# here we are chaining the .replace function
