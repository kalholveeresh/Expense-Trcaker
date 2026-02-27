import pandas as pd
import os

print("====Welcome to expense trcker====")


file_name="Expenses.csv"


if not os.path.exists(file_name):
    df=pd.DataFrame(columns=["date","category","description","amount"])
    df.to_csv(file_name,index=False)

while True:

    print("1. Add Expenses:")
    print("2. View all Expenses:")
    print("3. Total Expenses:")
    print("4. Exit:")


    choice=int(input("enter your choice:"))



    if(choice==1):
    
        date=input("enter the date spend money:")
        category=input("view all details of spend money:")
        description=input("Reason for spending money:")
        amount=float(input("how much money you spend:"))


        new_data=pd.DataFrame({
            "date":[date],
            "category":[category],
            "description":[description],
            "amount":[amount]
        })


        new_data.to_csv(file_name,mode="a",header=False,index=False)

        print("====Expense added Succesfully===")


    elif(choice==2):
        df=pd.read_csv(file_name)
        print(df)


    elif(choice==3):
        df=pd.read_csv(file_name)
        print("Total Spend money",df["amount"].sum())


    elif(choice==4):
        print("Exit from the code and no data added")
        break

    else:
        print("Invalid choice")
    


