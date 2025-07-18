# snake water gun game
import random

print("\t\t\tSnake  Water  Gun  Game")

# prints the loops of game
print(
'''
🐍 vs 💧 → 🐍 wins
💧 vs 🔫 → 💧 wins
🔫 vs 🐍 → 🔫 wins
🐍 vs 🔫 → 🔫 wins
💧 vs 🐍 → 🐍 wins
🔫 vs 💧 → 💧 wins
Same vs Same → Draw
'''
)

# initialised wins lose and draw with 0
win=0
lose=0
draw=0

# prints the options for game 
print("""1:🐍 s\n-1:💧 w\n0:🔫 g\n4:❌ e""")

# infite loop here
while(True): 
# initialised a dictonary and its reverse
    Youdict={"s":1, "w":-1,"g":0,"e":4}
    revdict={1: "snake", -1: "water", 0: "gun"}
# gets input from user
    you=input("Write the option as it is: ")
    choice=Youdict.get(you)

# if user chooses e choice will be 4 and we will exit program
    if choice==4:
        break

# choose a random number here between 0 numbers 
    computer=random.choice([1,-1,0])    
    
# if else ladder here for game logic
    if choice==computer:
        print("Draw")
        draw+=1
    elif(choice not in [1,0,-1]):
        print("Invalid choice")
        continue
    else:
        if (choice==1  and computer==-1): 
            print("You win.Congrats!")
            win+=1
        elif(choice==1 and computer==0): 
            print("Computer wins")
            lose+=1
        elif(choice==-1 and computer==1): 
            print("Computer win")
            lose+=1
        elif(choice==-1 and computer==0): 
            print("You win.Congrats!")
            win+=1
        elif(choice==0 and computer==1): 
            print("You win.Congrats")
            win+=1
        elif (choice==0 and computer==-1): 
            print("Computer win")
            lose+=1

# printed computer choice 
    print(f"Computer picked {revdict[computer]}")


# printed draw win and lose 
print(f"Win = {win}\nLose = {lose}\nDraw = {draw}")
