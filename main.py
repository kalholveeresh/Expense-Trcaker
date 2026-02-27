expenses=[] #list of expenses 
print(":-Track your Expense-: ")

while True:
    print("=====Menu=====")
    print("1.  Add Expenses:")
    print("2.  View all Expenses:")
    print("3.  Total  Expenses:")
    print("4.  EXIT:")

    choice=int(input("Enter your choice:"))

#Add Expenses
    if(choice==1):
        date=(input("Which date you spend money:"))
        category=input("where you spend amount:")
        Description=input("Describe spend money in details:")
        amount=float(input("eneter the amount how much you spend:"))

        expense={
            "date":date,
            "category":category,
            "description":Description,
            "amount":amount
        }


        expenses.append(expense)
        print("expenses added Succesfully:")

    
#View all Expenses

    elif(choice==2):
        if(len(expenses)==0):
            print("No Expense added, Spend some money and chill")
        else:
            print("======See all The expense=====")
            count=1
            for amount_spend in expenses:
                print(f"expense no{count}-->{amount_spend["date"]},{amount_spend["category"]},{amount_spend["description"]},{amount_spend["amount"]}")
                count+=1


# Total Expenses
    elif(choice==3):
        Total=0
        for spend_amount in expenses:
            Total=Total+spend_amount["amount"]

        print(f"Total spend amount:{Total}")

# Exit 
    elif(choice==4):
        print("------->>>Thank you for using Expense Tracker=====")
        break

    else:
        print("Invalid choice, Try again")



    