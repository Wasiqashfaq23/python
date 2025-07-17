# break means forget everything and exit loop
# continue means skip only this iteration and move forward
for i in range (100):
    if(i==34):
        break  # exit the loop right now
    print(i)


for i in range (100):
    if(i==34):
        continue  # skip only this iteration and move forward
    print(i)  


# when we dont want to use anything in for 

li=[1,2,3,4,5,6,6]

for i in li:
    pass  # null statement in pyhton instructs to do nothing


i=0
while(i<56):
    print(i)
    i+=1