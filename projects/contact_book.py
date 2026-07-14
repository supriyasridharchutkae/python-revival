contacts = []

def main():
    print("======CONTACT BOOK=====") 
    print("1 to add contact") 
    print("2 to view contact")
    print("3 to delete contact")
    print("4 to exit") 
    choice=int(input("enter your choice"))
    if choice==1:
        print(add_contact())
       
    elif choice==2:
        view_contact()
    elif choice==3:
        delete_contact()
    else:
        print("good bye")
        exit()
def add_contact():
    contact={
    "name":"",
    "phone_number":""}
    name=input("enter the name of ontact you want to add")
    if(name.isdigit()==True):
        print("enter a valid name")
        return "failure to add"
    for i in range(len(contacts)):
        for j in range(len(contacts)):
            if contacts[i]["name"]==contacts[j]["name"] or contacts[i]["phone_number"]==contacts[j]["phone_number"] :
                print("the contact already exists")
                return "failure to add"
    else:
        contact["name"]=name
    phone_number =input("enter the phone number")
    if(phone_number.isalpha()==True or  len(phone_number)!=10):
        print("enter valid number")
        return "failure to add"
    else:
        contact["phone_number"]=phone_number
        contacts.append(contact)
        return "contact succesfully added"


    
def delete_contact():
    name=input("pls enter the nma eof the contact you would like to delete")
    for i in range(len(contacts)):
        if contacts[i]["name"]==name: 
            contacts.pop(i)
            print("contact successfully deleted")
            break
def view_contact():
    name=input("enter the name of contact you would like to view")
    for i in range(len(contacts)): 
        if contacts[i]["name"]==name: 
            print("the name  is",contacts[i]["name"])
            print("the phone number is" ,contacts[i]["phone_number"])
            break

while(True):
    main()
    print(contacts)