st="I am Wasiq"

f=open("file.txt", "a")

f.write(st)

f=open("file.txt")
data=f.read()
print(data)

f.close
