# This script will prompt the user to enter a positive integer, 
# then use nested loops to print a square pattern of that size 
# made of asterisks (*).

size = int(input("Enter the size of the pattern: "))
i = 0
k = 0
while i < size:
    print("",end="")
    k = 0
    while(k < size):
        print("*",end="")
        k += 1
    i += 1
    print("")
