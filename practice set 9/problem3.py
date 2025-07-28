# write multiplication table from 2 to 20 and  sace them to different files and save that
# for a 13 year old


def generatetable(n):
    table=""
    for i in range(1,11):
        table+=f"{n} X {i} = {n*i}\n"
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)

    
for i in range(2,21):
    generatetable(i)