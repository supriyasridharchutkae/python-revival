def febonacci(number):
    first=0
    second=1
    for i in range(0,number):
        next=first+second
        if(i==0):
            print(first)
            print(second)
        else:
            print(next)
            first=second
            second=next

         
    

number=int(input("please enter the range of the number"))
febonacci(number)