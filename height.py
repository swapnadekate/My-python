print("*******************PROGRAM FOR HEIGHT*********************")
print("ENTER YOUR HEIGHT :  ")
ft=int(input("Height in feet :   "))
inch=int(input("Height in Inches :  "))


inch +=ft * 12
cm=round(inch * 2.54,1)




print("Your height is : %d cm." %cm)