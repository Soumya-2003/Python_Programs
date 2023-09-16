# Write a program to input N numbers and then print the second largest number.
n = int(input("Enter the no. of inputs: "))
max1 = max2 = 0
for i in range(0,n):
    num = int(input("Enter input: "))
    if (num > max1):
        max2 = max1
        max1 = num
        
    else:
        if(num > max2):
            max2 = num
            
print("Second largest number is:",max2)