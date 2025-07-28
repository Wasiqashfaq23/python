f=open("file.txt")

# lines=f.readlines()
# print(lines,type(lines))
# # readlines returns list of lines

# line1=f.readline()
# print(line1,type(line1))

# line2=f.readline()
# print(line2,type(line2))

# line3=f.readline()
# print(line3,type(line3))

# line4=f.readline()
# print(line4,type(line4))
      
# # as their is no 5th line in the txt file so it returns an empty string 
# # we can check that by using  print(line5=="") as it will return true
# line5=f.readline()
# print(line5,type(line5))
# print(line5=="")



# if we want to do that in loop 
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()

f.close()

# modes of opening a file
'''
r    =   read(default)

w    =   open for writing

a    =   open for appending   #appending mean inserting in the last of file

+    =   open for updating

rb   =   open for read in binary mode

rt   =   open for read in text mode

'''