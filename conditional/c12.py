print ("****** CALCULATOR *******")
print("Menu ")
print("1. ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4. DVISION")

choice = int(input("enter your choice (1-4) : "))
a = int(input("enter first number : "))
b = int(input("enter second number : "))

match choice :
    case 1 :
        print(a+b)
    case 2 :
        print(a-b)
    case 3 :
        print(a*b)
    case 4 :
        if b==0:
            print("nuber is not divisible by zero")
        else:
            print (a/b)
    case _ :
        print("invalid choice!  ")
