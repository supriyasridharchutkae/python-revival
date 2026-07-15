expenses=[]
def main():
    print("======EXPENSE TRACKER======")
    print("1. Add expense")
    print("2. Delete expense")
    print("3. View expense")
    print("4. Total expenses")
    print("exit")
    choice=int(input("Enter choice "))
    if choice==1:
        add_expense()
    elif choice==2:
        delete_expense()
    elif choice==3:
        view_expense()
    elif choice==4:
        total_expenses()
    else:
        print("Good bye!")
        exit()
        


def add_expense():
    expense={}
    cat=["food","travel","shopping"]
    print("the valid categories are :\n food\ntravel\nshopping\n")
    category=input("Please enter the category you would like to add")
    while True:
        if category.isalpha() and category in cat:
            amount=int(input("Please enter the amount you would like to add"))
            expense["amount"]=amount
            expense["category"]=category
            expenses.append(expense)
            break
        else:
            print("please enter the a correct category")
            category=input("Please enter the category you would like to add")
    

    
def delete_expense():
   category= input("which caegory  would you liek to delete")
   cat=["food","travel","shopping"]
   length=len(expenses)
   while True:
    if(category not in cat  ):
        print("enter valid category")
        break
    for i in range(length):
        if(expenses[i]["category"]==category):
            expenses.pop(i)
            break
    if len(expenses)<length:
        print("sucessfully deleted")
        break
    else:
        print("not sucessfully deleted")

def total_expenses():
    total=0
    for expense in expenses:
        total=expense["amount"]+total
    print(f"teh total is {total}")

    
def view_expense():
    expense_category=input("enter the expense you would like to view")
    
    print(len(expenses))
    
    for expense in expenses:
        if(expense["category"]==expense_category):
            print(f"category {expense_category} \namount {expense['amount']}")
        
                    
    
    

    


while(True):
    main()
    