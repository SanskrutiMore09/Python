ATM = int(input("Enter your ATM Number:"))
PIN = int(input("Enter your PIN:"))
if ATM==123456 and PIN==1234:
    print("\n ATM menu \n 1. Balance Enquiry \n 2. Cash Withdrawl \n 3. Cash Deposit \n 4. Exit")
choice = int(input("Enter your choice:"))
if choice==1:
    print("Your balance is 1000")
elif choice==2:
    print("Enter amount to withdraw:")
    amount = int(input())
elif choice==3:
    print("Enter amount to deposit:")
    amount = int(input())
elif choice==4:
    print("Thank you for using our ATM") 
else:
    print("Invalid ATM or PIN")