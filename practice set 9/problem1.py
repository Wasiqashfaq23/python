# write a program to read text from a given file poems.txt and 
# find out wether or not it contains word
# "Twinkle"
word="Twinkle"
with open("poems.txt") as f:
    content=f.read()
    if((word in content)==True):
        print("Yes Twinkle is present in content")
    else:
        print("NO")