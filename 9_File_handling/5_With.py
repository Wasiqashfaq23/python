f=open("file.txt")

print(f.read())

f.close()

# the same can be written using with statement like this
# and we dont have to seperately close the file after with statement
 
with open("file.txt") as f:
    print(f.read)