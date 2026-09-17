# without recursion -- factorial
def factorial(n):
    
    if n < 0:
        print("Factorial does not exist for negative numbers.")
    else:
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
    print("Result:", fact)

n = int(input("Enter a positive integer: "))
factorial(n)

# with recursion -- factorial
def factorial (n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))