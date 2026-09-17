print("Menu ")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

balance = 40000
choice = int(input("enter your choice (1-4) : "))
a = int(input("enter your choice : "))

match choice :
    case 1 :
        print(balance)
    case 2 :
        deposit = int(input("enter your deposit amount : "))
        balance = balance + deposit
        print(f"deposited..! your banlance now is {balance} " )
    case 3 :
        withdraw = int(input("enter your Withdraw amount : "))
        if(balance < withdraw) :
            balance = balance - withdraw
            print(f"withdrawn..! your banlance now is {balance} " )
        
    case 4 :
            print("exited....")
            
    case _ :
        print("invalid choice!  ")
