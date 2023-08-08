# bank simple system

menu = """

[d] Deposit
[w] Withdraw
[t] Transactions
[q] Quit

=> """

balance = 0
limit = 500
transactions = ""
qt_withdraw = 0
withdraw_limit = 3

while True:

    option = input(menu)

    if option == "d":
        amount = float(input("Inform deposit value: "))

        if amount > 0:
            balance += amount
            transactions += f"Deposit: € {amount: .2f}\n"

        else:
            print("Failed transaction. Invalid amount informed")

    elif option == "w":
        amount = float(input("Inform the desired amount: "))

        exceeded_withdraw = amount > balance

        exceeded_limit = amount > limit

        exceeded_qt_withdraw = qt_withdraw >= withdraw_limit

        if exceeded_withdraw:
            print("Failed operation: There is no enough balance")

        elif exceeded_limit:
            print(f"Failed operation: Your limit is {limit: .2f}\n")
        
        elif exceeded_qt_withdraw:
            print("Failed operation: Exceeded quantity of daily withdraws")

        elif amount > 0:
            balance -= amount
            transactions += f"Withdraw: € {amount: .2f}\n"
            qt_withdraw += 1


    elif option == "t":
        print("\n******* TRANSACTION LOGS *******")
        print("There is no operation in the desired period." if not transactions else  transactions)
        print(f"\nBalance: € {balance:.2f}")
        print("**************************")

    elif option == "q":
        break

    else:
        print("Invalid option. Please chose again the desired option")

    