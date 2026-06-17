#This is a Signup/Login System but because there is no database i will use while loop to keep the code running
# and will make sure that data stores in dictionary temporarily...
while True:
    try:
        print("----RANDOM COMPANY APP----")
        print("Press 1: For Signup")
        print("Press 2: For Login")

        choose = int(input("Choose Option: "))

        if choose == 1:
            signup()
        elif choose == 2:
            login()
    except:
        print("...Please Enter Valid Value...")