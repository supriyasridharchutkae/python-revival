class EvenOdd:
    def new_func(self,a):
        if(a%2==0):
            return "even"
        else:

            return "odd"

evo=EvenOdd()
input1=int(input("pls enter a number:"))
print(evo.new_func(input1))