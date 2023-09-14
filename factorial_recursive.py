# Write a program to find the factorial of a number using a recursive method

def factorial(num):
    if (num == 1):
        return num
    else:
        return (num * factorial(num-1))
    
n = int(input("Enter the no.: "))
if(n < 0):
    print("Factorial does not exist")
elif (n == 0):
    print("Factorial of",n,": 1")
else:
    print("Factorial of",n,":",factorial(n))