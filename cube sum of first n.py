# Program to print cube sum of first n natural numbers
n = int(input("Input the value of n: "))
s = 0
# iterating loop up to given number n
for i in range(1,n+1):
	s = s + (i**3)
print("Cube Sum is: ",s)