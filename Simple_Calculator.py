#This is a simple calculator that takes values from user and perform operations on them..
try:
    print("------WELCOME TO SIMPLE CALCULATOR------")
    print("Note: All the simple mathematical operations like\n*Addition\n*Subtraction\n*Multiplication\n*Division\n*Floor Division\nCan be performed by this calculator")
    print(50*"-")
    fnum = int(input("Enter First Number: ").strip())
    snum = int(input("Enter Second Number: ").strip())
    print(50*"-")
    print("Here are the results")
    print(f"{fnum}+{snum} = {fnum+snum}")
    print(f"{fnum}-{snum} = {fnum-snum}")
    print(f"{fnum}*{snum} = {fnum*snum}")
    print(f"{fnum}/{snum} = {fnum/snum}")
    print(f"{fnum}//{snum} = {fnum//snum}")
except ZeroDivisionError:
    if fnum == 1 and snum == 0:
        print("...I know what you are trying to do here lad...")
except ValueError:
    print("...Please Enter Valid Values (Only Numerical Values)...")
#Desc: Used print(50*"-") for a little bit design and f-string for avoiding execcisive writing 
#       try and except is used for error handling if someone tries to enter alphabets or symbols in input field
#       and someone tries to do 1/0 for ongoing loop and someone tries to give no values 
