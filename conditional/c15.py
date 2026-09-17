a=input("Enter rock, paper or scissors: ")
b=input("Enter rock, paper or scissors: ")
if a==b:
     print("Draw")
elif a=="rock" and b=="scissors":
     print("Player 1 wins") 
elif a=="scissors" and b=="paper":
    print("Player 1 wins")
elif a=="paper" and b=="rock":
    print("Player 1 wins")
else:
     print("Player 2 wins")