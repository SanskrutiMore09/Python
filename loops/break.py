# break keyword.......
correct_pass ="some_pass"
while True: 
    string = input("enter a string : ")
    if string == correct_pass:
        break
    else:
        print("wrong password try again !!!")
print("password matched!!")