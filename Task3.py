def withdraw(balance, amount):
    if amount > 0 and amount <= balance and amount % 500 == 0:
        balance = balance - amount
        return balance
    else:
        return balance

correct_pin = "1234"
pin = input("Enter your PIN: ")

if pin != correct_pin:
    print("Access denied")
else:
    balance = int(input("Enter your account balance: "))

    while True:
        amount = int(input("Enter withdrawal amount (0 to exit): "))

        if amount == 0:
            print("Exit from program")
            break
        if amount <= 0:
            print("Amount should greater than 0")
        elif amount > balance:
            print("Insufficient balance")
        elif amount % 500 != 0:
            print("Amount must be a multiple of 500")
        else:
            balance = withdraw(balance, amount)
            print("Withdrawal successful")
            print("Remaining balance= ", balance)