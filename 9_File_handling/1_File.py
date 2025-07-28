# we do file io if we want to store a data and later use that data for a specific purpose 
# there are two types of files 
# 1.binary file
# 2.txt file     py is a txt file 


f=open("file.txt")
data=f.read()
print(data)
f.close()