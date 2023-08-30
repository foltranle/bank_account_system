import textwrap


def menu():
    menu = """\n
    -------------------- MENU --------------------
    [d]\tDeposit
    [s]\tWithdraw
    [t]\ttransactions
    [q]\tQuit
    => """
    return input(textwrap.dedent(menu))


def Deposit(balance, amount, transactions, /):
    if amount > 0:
        balance += amount
        transactions += f"Deposit:\tR$ {amount:.2f}\n"
        print("\n---- Successful deposit! ----")
    else:
        print("\n---- Failed operation. Choose a valid option. ----")

    return balance, transactions


def Withdraw(*, balance, amount, transactions, account_limit, qt_withdraw, withdraw_limit):
    exceeded_withdraw = amount > balance

    exceeded_limit = amount > limit

    exceeded_qt_withdraw = qt_withdraw >= withdraw_limit

    if exceeded_withdraw:
        print("\n---- Failed operation. Insufficient funds. ----")

    elif exceeded_limit:
        print("\n---- Failed operation. Withdraw limit exceeded. ----")

    elif exceeded_saques:
        print("\n---- Failed operation. Withdraw limit reached. ----")

    elif amount > 0:
        balance -= amount
        transactions += f"Withdraw:\t\tR$ {amount:.2f}\n"
        qt_withdraw += 1
        print("\n---- Successful withdraw! ----")

    else:
        print("\n---- Failed operation. Chose a valid amount. ----")

    return balance, transactions


def exibit_transactions(balance, /, *, transactions):
    print("\n--------------------- transactions ---------------------")
    print("Não foram realizadas movimentações." if not transactions else transactions)
    print(f"\nbalance:\t\tR$ {balance:.2f}")
    print("--------------------------------------------------------")


def main():
    withdraw_limit = 3
    agency = "0001"

    balance = 0
    limit = 500
    transactions = ""
    qt_withdraw = 0
    

    while True:
        option = menu()

        if option == "d":
            amount = float(input("Inform deposit amount: "))

            balance, transactions = deposit(balance, amount, transactions)

        elif option == "s":
            amount = float(input("Inform withdraw amount: "))

            balance, transactions = Withdraw(
                balance=balance,
                amount=amount,
                transactions=transactions,
                limit=limit,
                qt_withdraw=qt_withdraw,
                withdraw_limits=withdraw_limits,
            )

        elif option == "t":
            exibit_transactions(balance, transactions=transactions)

        
        elif option == "q":
            break

        else:
            print("Invalid operation. Chose a valid one")


main()