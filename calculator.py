class Calculator:

    def add(self,a,b):
        print((a+b))
    def subtract(self,a,b):
        print((a-b))
    def multiply(self,a,b):
        print((a*b))
    def divide(self,a,b):
        print((a/b))

input1=int(input("pls enter 1st number:"))
input2=int(input("pls enter 2nd number:"))
input3=int(input("which operation you want to perform: 1.add 2.subtract 3.multiply 4.divide"))
cal= Calculator()
if(input3==1):
    cal.add(input1,input2)
elif(input3==2):
    cal.subtract(input1,input2)
elif(input3==3):
    cal.multiply(input1,input2)
elif(input3==4):
    cal.divide(input1,input2)
