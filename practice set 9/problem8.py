# write a program to make a copy of file main.txt 

with open("main.txt") as f:
    content=f.read()

with open("_main_copy.txt", "w") as f:
    content=f.write(content)