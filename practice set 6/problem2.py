# write a program to find wether a student is pass if it require 40% total and 33% in each subject to pass 
# assume 3 subjects as input


Subject_1=int(input("Enter Marks of Math: "))
Subject_2=int(input("Enter Marks of Physics: "))
Subject_3=int(input("Enter Marks of Chemistry: "))

sum=float(Subject_1+Subject_2+Subject_3)
Total_percentage=float(sum/3)

if(Total_percentage>=40.0 and Subject_1>=33.0 and Subject_2>=33.0 and Subject_3>=33.0 ):
    print("Pass , Good for you" , Total_percentage )
else:
    print("Fail , Try again next time",Total_percentage)
