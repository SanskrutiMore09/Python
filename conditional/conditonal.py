# is_Raining = True 
# if is_Raining:
#     print("Raining Outside")
# else:
#     print("Not Raining")

# is_Raining = False 
# if is_Raining:
#     print("Raining Outside")
# else:
#     print("Not Raining")

# age=int(input("enter your age : "))
# if age>=18:
#     print("Eligible to vote")
# else:
#     print("Not Eligible to vote")

# n=int(input("Enter number : "))
# if n==1:
#     print("Sunday")
# elif n==2:
#      print("Monday")
# elif n==3:
#      print("Tuesday")
# elif n==4:
#      print("Wednessday")
# elif n==5:
#      print("Thursday")
# elif n==6:
#      print("Friday")
# elif n==7:
#      print("Saturday")
# else:
#      print("Invalid no.")

# age = 20
# has_id = True

# if age >= 18 :
#     if has_id :
#         print("Entry Allowed")
#     else:
#         print("Id Required")
# else :
#     print("Underage")


# even odd
# a=int(input("enter your number : "))
# if a%2==0 :
#     print("Even")
# else :
#     print("odd")

# age = int(input("enter your age : "))
# ticket = 200
# if age<=12 :
#     ticket = ticket-(ticket*0.10)
#     print(f"your ticket price is {ticket}")
# else :
#     print(f"your ticket price is {ticket}")

# marks = int(input("enter your marks : "))

# if marks<=100 and marks>=90 :
#     print("O GRADE")
# elif marks<=89 and marks>=80 :
#      print("A GRADE")
# elif marks<=79 and marks>=65 :
#      print("B GRADE")
# elif marks<=64 and marks>=35 :
#      print("C GRADE")
# elif marks<=34 and marks>=0 :
#      print("FAIL")
# else :
#      print("enter between 1 to 100")


# a=int(input("enter your number : "))
# if a<0 :
#     print("NEGATIVE")
# elif a>0 :
#     print("POSITIVE")
# else :
#     print("ZERO")
    
# a=int(input("enter your number : "))
# b=int(input("enter your number : "))
# c=int(input("enter your number : "))
# if a>b and a>c :
#     print("a is GREATER")
# elif b>a and b>c :
#     print (" b is GREATER")
# elif c>a and c>b :
#     print("c is GREATER")
# elif a==b or a==c : 
#     print ("two no.are equal")
# elif b==a or b==c : 
#     print ("two no.are equal")
# elif a==b or a==c : 
#     print ("two no. are equal")
# else :
#     print("invalid")

# year=int(input("enter year : "))

# if year%4==0 :
#     print("leap year")
# else :
#     print("not a leap year")

# print ("****** CALCULATOR *******")
# print("Menu ")
# print("1. ADDITION")
# print("2.SUBTRACTION")
# print("3.MULTIPLICATION")
# print("4. DVISION")

# choice = int(input("enter your choice (1-4) : "))
# a = int(input("enter first number : "))
# b = int(input("enter second number : "))

# match choice :
#     case 1 :
#         print(a+b)
#     case 2 :
#         print(a-b)
#     case 3 :
#         print(a*b)
#     case 4 :
#         if b==0:
#             print("nuber is not divisible by zero")
#         else:
#             print (a/b)
#     case _ :
#         print("invalid choice!  ")

# print("traffic signal")
# color = input("enter color (red/yellow/green) : ")
# if color=="red":
#     print("stop")
# elif color=="yellow":
#     print("get ready")
# elif color=="green":
#     print("go")
# else:
#     print("enter valid color")


# print("Menu ")
# print("1. Check Balance")
# print("2. Deposit")
# print("3. Withdraw")
# print("4. Exit")

# balance = 40000
# choice = int(input("enter your choice (1-4) : "))
# a = int(input("enter your choice : "))

# match choice :
#     case 1 :
#         print(balance)
#     case 2 :
#         deposit = int(input("enter your deposit amount : "))
#         balance = balance + deposit
#         print(f"deposited..! your banlance now is {balance} " )
#     case 3 :
#         withdraw = int(input("enter your Withdraw amount : "))
#         if(balance < withdraw) :
#         balance = balance - withdraw
#         print(f"withdrawn..! your banlance now is {balance} " )
        
#     case 4 :
#         if b==0:
#             print("nuber is not divisible by zero")
#         else:
#             print (a/b)
#     case _ :
#         print("invalid choice!  ")


# a=input("Enter rock, paper or scissors: ")
# b=input("Enter rock, paper or scissors: ")
# if a==b:
#      print("Draw")
# elif a=="rock" and b=="scissors":
#      print("Player 1 wins") 
# elif a=="scissors" and b=="paper":
#     print("Player 1 wins")
# elif a=="paper" and b=="rock":
#     print("Player 1 wins")
# else:
#      print("Player 2 wins")

# ATM = int(input("Enter your ATM Number:"))
# PIN = int(input("Enter your PIN:"))
# if ATM==123456 and PIN==1234:
#     print("\n ATM menu \n 1. Balance Enquiry \n 2. Cash Withdrawl \n 3. Cash Deposit \n 4. Exit")
# choice = int(input("Enter your choice:"))
# if choice==1:
#     print("Your balance is 1000")
# elif choice==2:
#     print("Enter amount to withdraw:")
#     amount = int(input())
# elif choice==3:
#     print("Enter amount to deposit:")
#     amount = int(input())
# elif choice==4:
#     print("Thank you for using our ATM") 
# else:
#     print("Invalid ATM or PIN")