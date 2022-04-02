@pylint score (5.12/10)

import re

# Creating variables for ATM system
import self as self

ID = ['id1', 'id2', 'id3']
pins = ['1111', '2222', '3333']
amounts = [5000, 5500, 6000]
count = 0
opr = [1, 2, 3, 4]


class ATM:
    # Input from the user/
    def __init__(self, id, pin, amount):
        self.id = id
        self.pin = pin
        self.amount = amount


class Validation:

    # Verification of user ID/
    def check_id():

        check_id = ['id1', 'id2', 'id3']
        user = str(input("Enter your ID from following id's \n id1, id2, id3: "))
        if user in check_id:
            print("*VALID ID*")
        else:
            print("!INVALID ID!")
        return user

    w = check_id()

    # Validation of phone number/

    def check_phn(s):
        # 1) Starts with 0 or 91.
        # 2) It shall contain 6 - 9 as first number.
        # 3) It shall contain 9 digits.
        Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
        return Pattern.match(s)

    # Driver Code

    s = input("Enter registered phone number: ")
    if check_phn(s):
        print("*VALID PHONE NUMBER*")
    else:
        print("Invalid Number")

        # Validation of pin/

    def check_pin(self):
        check_pin = ['1111', '2222', '3333']
        global user2
        user2 = str(input("Enter your pin: "))
        if user2 in check_pin:
            print("Valid pin!")
        else:
            print("InValid pin!")
        return user2

    check_pin(self)

    print("*WELCOME TO ATM SYSTEM*")
    print("------------------------")
    print("SELECT OPERATION FROM THE FOLLOWING LIST: ")
    print("-------------------------------------")
    print("1. AVAILABLE ACCOUNTS DETAILS.")
    print("2. CASH WITHDRAWAL.")
    print("3. CASH DEPOSIT.")
    print("4. PIN CHANGE.")

    def check_opr():
        global amounts, amounts
        user = 1
        check_opr = [1, 2, 3, 4]
        while user >= 1 and user <= 4:
            user = int(input("ENTER OPERATION: "))
            if user in check_opr:
                if user == 1:
                    print("These are all data in this ATM machine")
                    print("------------------------------")
                    print(f"ID's available are: {ID}")
                    print(f"PIN's available are: {pins}")
                    print("******************************")
                if user == 2:
                    wd_amount = int(input("Enter the amount you want to withdraw: \n"))
                    print("----------------------------------------")
                    amounts = amounts - wd_amount
                    print(f"{wd_amount} debited from your account \n")
                    print(f"Your updated account balance is {amounts}")
                    print("******************************************")
                if user == 3:
                    deposit_cash = int(input("Enter the amount to deposit: \n"))
                    print("-----------------------------------------")
                    amounts = amounts + deposit_cash
                    print(f"{deposit_cash} credited from your account \n")
                    print(f"Your updated account balance is {amounts}")
                    print("******************************************")
                if user == 4:
                    pin_change = str(input("Enter your new pin: \n"))
                    print("------------------------")
                    var = pin == pin_change
                    print(f"Your new pin is {pin_change}")
                    print("*****************************")
                if user < 1 or user > 4:
                    print("Invalid Input")

    check_opr()
    print(w)
    print(s)
