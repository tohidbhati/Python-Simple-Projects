#This is a star patter project where it will use value given by user to print various types of star pattern and it will also asks user that which type of pattern they wants..

print("-----WELCOME TO STAR PATTERN------")
print("It will also asks user that which type of pattern they wants..")
print("Press 1: For Simple Square Pattern")
print("Press 2: For Simple Rectangle Pattern")
print("Press 3: For Simple Equilateral Triangle Pattern")
print("Press 4: For Simple Rhombus Pattern")
print("Press 5: For Simple Circle Pattern")
print("Press 6: For Simple Star Pattern")
print("Press 7: For Christmas Tree Pattern")

choice = int(input("Choose Value: "))
valueFor_Star = int(input("Enter Value: "))

for i in range(1,valueFor_Star):
    print("*"*valueFor_Star)