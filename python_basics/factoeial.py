def factorial(number):
    print(f"the factorial of {number} is:")
    factorial=1
    for i in range(1,number+1):
       factorial*=i
    return factorial

number=int(input("please enter the number you wantt the factorial of"))
print(factorial(number))

