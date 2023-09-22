# Write a program to print a inverted full pyramid of *.
row = int(input("Input the no. of row: "))
for i in range(0,row):
    for space in range(0,i):
        print(" ",end="")
    for star in range(0,row-i):
        print("* ",end="")
    print("\t")
        