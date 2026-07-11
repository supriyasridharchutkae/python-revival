def largest_number(n1,n2,n3):
    if n1==n2 or n2==n3 or n1==n3:
        print("two numbers are the same", n1) 
    if(n1>=n2 and n1>=n3 ):
        return n1
    elif(n2>=n1 and n2>=n3):
        return n2
    elif(n3>=n1 and n3>=n2):
        return n3
    else:
        return "all numbers are teh same"
    
    

number1=int(input("enter the 1st number:"))
number2=int(input("enter the 2nd number:"))
number3=int(input("enter the 3rd number:"))
print("the largest number is:"+str(largest_number(number1,number2,number3)))



