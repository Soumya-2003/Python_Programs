# Program for finding n-th Fibonacci number Using recursion
def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

N = int(input("Input the value of N: ")) 
print(N,"-th Fibonacci No.:",Fibonacci(N))