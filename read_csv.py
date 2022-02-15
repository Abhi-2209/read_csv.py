import csv
import datetime
import os.path


def display():
    with open("Transactions.csv", 'r') as obj:
        fobj = csv.reader(obj)
        for i in fobj:
            print(i)


def write_transaction():
    with open("Transactions.csv", 'a', newline="") as obj:
        fobj = csv.writer(obj)
        desc = input("Enter Description")
        amt = int(input("Enter Amount(income/expense)"))
        dte = input("Enter Date of Transaction (DD/MM/YYYY)")
        dte2 = datetime.datetime.strptime(dte, "%d/%m/%Y")
        record = [desc, amt, dte]
        fobj.writerow(record)
        print("Transaction saved to the file")
        budget()


def append():
    c = 1
    while c == 1:

        ch = int(input("\n 1-RECORD A TRANSACTION \n 2-CALCULATE THE CURRENT BUDGET \n 3-EXIT THE PROGRAM \n ENTER "
                       "CHOICE : "))
        if ch == 1:
            write_transaction()
        elif ch == 2:
            budget()
        else:
            quit()


def budget():
    print("current budget is ")



'''def search():
    roll = int(input("Enter number to search"))
    with open("details.csv", 'r') as obj:
        fobj = csv.reader(obj)
        next(fobj)
        for i in fobj:
            if i[0] == roll:
                print(i)
                x = x+1
        x = 0
        print("Data not found")'''

''''if os.path.isfile("details.csv"):
    append()'''

display()
append()

display()
