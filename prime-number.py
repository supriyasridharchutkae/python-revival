def Prime_Number(number):
    if(number >1):
        counter=0
        for i in range(1,number+1,1):
            if number%i==0:
                counter+=1
    else:
        return "enter a whole number please"

    if(counter==2):
        print("the number is  a prime")
    else:
        print("the number is not a prime")

number=int(input("pls enter the number"))
Prime_Number(number)