# write a program to calculate grade from marks 
# 90-100%  Extraordinary
# 80-90    A
# 70-80    B
# 60-70    C
# 50-60    D
# <50      F


marks=int(input("Enter your marks: "))
if(marks>=90 and marks<=100):
    print("Extraordinary")
elif(marks>=80 and marks<90):
    print("A")
elif(marks>=70 and marks<80):
    print("B")
elif(marks>=60 and marks<70):
    print("C")
elif(marks>=50 and marks<60):
    print("D")
elif(marks>=0 and marks<50):
    print("F")
else:
    print("Enter valid marks")