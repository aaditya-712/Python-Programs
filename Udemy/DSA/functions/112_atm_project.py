# ATM project

def atm(card_no):
    balance = 10000.00
    user_pin = 123456

    print("Checking if the card is valid...")
    if len(card_no) == 12:
        print("Card is valid...")
        pin = int(input("Enter PIN: "))

        if pin == user_pin:
            print("PIN authentication completed...")

            while True:
                print("\n1. Withdraw Money \n2. Check Balance \n3. Exit \n")
                try:
                    choice = int(input("Enter Choice: "))
                except ValueError:
                    print("Invalid Choice, Please enter a number.")
                    continue
                if choice == 1:
                    withdraw_amount = float(input("Enter amount to withdraw: "))
                    if not withdraw_amount <= balance:
                        print(f"Withdrawing INR. {withdraw_amount}")
                        balance -= withdraw_amount
                        print("Take your cash")
                        print(f"Remaining Balance: {balance:.2f}")
                    else:
                        print("Insufficient Balance")
                elif choice == 2:
                    print("Balance: ", balance)
                elif choice == 3:
                    print("Thank you for using ATM services!!!")
                    break
                else:
                    print("Invalid Choice")

        else:
            print("Incorrect PIN !!!")
    else:
        print("Card is invalid")


card_num = input("Enter your 12 digit atm number: ")
atm(card_num)

