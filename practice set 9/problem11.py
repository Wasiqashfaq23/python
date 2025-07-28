# write a python program to rename a file 

# one simple method to do that is by creating a copy of 
# original file and then delete the old file

with open("old.txt") as f:
    content=f.read()

with open("renamed.txt" , "w") as f:
    f.write(content)

# now to delete the file we can use os module 
# havent learned that yet