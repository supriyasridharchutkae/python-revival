

def funct(number,limit):
    for i in range(1,limit+1,1):
        print(str(i),"*",str(number),"=",str(i*number))
number=int(input("plese enter the number you want the multiplicationtable of:"))
limit=int(input("please enter the limit of the multiplication table:"))
print("the multiplication table of "+str(number)+" is:")
funct(number,limit)