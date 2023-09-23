# Program to find GCD of two numbers.
def gcd(a, b):
   if a == b:
      return a
   elif a < b:
      return gcd(b, a)
   else:
      return gcd(b, a - b)

a = int(input("Input a no.: "))
b = int(input("Input another no.: "))
print("GCD (",a,",",b,"):",gcd(a, b))