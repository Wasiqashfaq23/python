# write a program to remove a given word and strip it at the same time



def rem(l,word):
    n=[]
    for item in l:
        if not(item ==word):
            n.append(item.strip(word))
    return n


l=["Harry","Wasiq","Wamiq","Usama","Ashfaq"]

print(rem(l,"Ashfaq"))