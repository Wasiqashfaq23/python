# write a program to mine log file and check if it contains python or not

with open("log.txt") as f:
    content=f.read()

if ("python" in content):
    print("Yep it is here")
else:
    print("Go Went gone")