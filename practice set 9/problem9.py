# write a program to compare 2 files as are they same or not


with open("main.txt") as f:
    first=f.read()

with open("_main_copy.txt") as f:
    second=f.read()

if(first==second):
    print("Yes they are identical ")
else:
    print("GO went gone")