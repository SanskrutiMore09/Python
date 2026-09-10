print("hello world")
a=10
b='a'
c=True
d=2.56
e=6//2.3
print(e)

a=int(input("enter your number : "))
print(type(a))
b=20
c=a+b
print(c)

d=input("enter your name : ")

a=int(input("enter your number : "))
print(f"the number is odd : {a%2==0}")

age=20
print(f" {age} years = {age*365} days")

minutes = int(input("enter minutes : "))
print(f"{minutes} is {minutes//60} hours {minutes%60} minutes")

a=int(input("enter your number : "))
print(f"{a} : last digit is {a%10}")

a=input("enter your number : ")   #this is via string 
print(f"{a} : last digit is {a[-1]}")


role = input("enter your role :")
age = int(input("enter your age :"))
print(f" Eligible : {role.lower == 'student' and age < 21 }")

a=10
b=20
print(f" Before swap a = {a} b = {b}")
print(f" After swap a = {(a+b)-a} b = {(a+b)-b}")
a,b=b,a # direct swaping in python
#sanskruti more
#new comment
#hiiiiiii