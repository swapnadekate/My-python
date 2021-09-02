# PROGRAM TO SWAP THIRD VARIABLE
a = int(input("ENTER THE FIRST VARIABLE::   ")) 
b = int(input("ENTER THE SECOND VARIABLE::   "))
c = int(input("ENTER THE THIRD VARIABLE::   ",))

print("Value of A Before swapping : ",a)
print("Value of B before swapping : ",b)
print("Value of C before swapping : ",c)

temp=a
a=b
b=c
c=temp
print("Value of A After swapping : ",a)
print("Value of B After swapping : ",b)
print("Value of C After swapping : ",c)
