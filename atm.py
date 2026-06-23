print("--WELCOME TO ATM--")

users = ['Abhi', 'Ankit', 'Mahi', 'Ankit']
pins = [1234, 2345, 5555, 8888]
balance = [20000, 65000, 70000, 20000]

pin = int(input("Enter Your PIN: "))

if pin in pins:
    index = pins.index(pin)

    print(f"Welcome {users[index]}")
    print("What would you like to do?")

    while True:
        print("\nPress 1. For Account Status")
        print("Press 2. For Cash Withdrawal")
        print("Press 3. For PIN Change")
        print("Press 4. For Cash Deposit")
        print("Press 5. For Exit")

        choose = int(input("Choose Option: "))

        if choose == 1:
            print(f"Account Name: {users[index]}")
            print(f"Total Balance: ₹{balance[index]}")

        elif choose == 2:
            withdrawal = int(input("Enter Amount To Withdraw: "))

            if withdrawal <= balance[index]:
                balance[index] -= withdrawal
                print(f"₹{withdrawal} withdrawn successfully.")
                print(f"Available Balance: ₹{balance[index]}")
            else:
                print("Insufficient Balance!")

        elif choose == 3:
            current_pin = int(input("Enter Current PIN: "))

            if current_pin == pins[index]:
                new_pin = int(input("Enter New PIN: "))
                pins[index] = new_pin
                print("PIN changed successfully!")
            else:
                print("Incorrect Current PIN!")

        elif choose == 4:
            deposit = int(input("Enter Amount To Deposit: "))
            balance[index] += deposit
            print(f"₹{deposit} deposited successfully.")
            print(f"New Balance: ₹{balance[index]}")

        elif choose == 5:
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid Option!")

else:
    print("Invalid PIN!")