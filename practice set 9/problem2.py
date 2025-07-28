# write a game function returns an int whose score is saved in Hi-score.txt
# update the file when the highscore is beaten 

import random

def game():
    # start of function
    print("You are playing the game")
    # generating a random score
    score=random.randint(1,62)
    # reading file for hiscore
    with open("Hi-score.txt") as f:
        hiscore=f.read()
        # if file is not empty get the hiscore from there as a int
        if (hiscore!=""):
            hiscore=int(hiscore)
        # if file is empty let hiscore = 0 
        else:
             hiscore=0
    # printing score
    print("Your score is ",{score})
    # if score is greater than hiscore we write the new score
    if(score>hiscore):
        with open("Hi-score.txt","w") as f:
            f.write(str(score))
    # returened the integer
    return score

 
game()  