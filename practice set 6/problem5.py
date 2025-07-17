# check wether a given number is present in list or not

list=["Saqaf","Usama","Wasiq","Hello","Usman","Haseeb","Ahsan","Burhan"]

name=input("Enter username to detect presence: ")

if(name in list):
    print("Your name is in the list")
else:
    print("Name not present")