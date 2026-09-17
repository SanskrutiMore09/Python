marks = int(input("enter your marks : "))

if marks<=100 and marks>=90 :
    print("O GRADE")
elif marks<=89 and marks>=80 :
     print("A GRADE")
elif marks<=79 and marks>=65 :
     print("B GRADE")
elif marks<=64 and marks>=35 :
     print("C GRADE")
elif marks<=34 and marks>=0 :
     print("FAIL")
else :
     print("enter between 1 to 100")
