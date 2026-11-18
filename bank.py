def bankOper(initialBal, deposit, withdraw):
    totalBal = initialBal + deposit
    updatedBal = totalBal - withdraw

    return totalBal, updatedBal

if __name__== "__main__":
    initialBal = int(input("Enter amount as initial: "))
    deposit = int(input("Enter amount to deposit: "))
    withdraw = int(input("Enter withdraw amount: "))

    totalBal, updatedBal = bankOper(initialBal, deposit, withdraw)

    print("Total Balance: ",totalBal)
    print("Updated Balance: ",updatedBal)