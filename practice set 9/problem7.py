# write a program to check for the line number where their is python written
# as from question 6

lineno=1
with open("log.txt") as f:
    lines=f.readlines()

for line in lines:
    if ("python" in line):
        print("Yep it is here , line no" , lineno)
        break
    lineno+=1   
else:
    print("Go Went gone")