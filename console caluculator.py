import module1
import module3
print("******CALUCULATOR******")
while True:
    print("please choose the option")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.power")
    print("6.square root")
    choice = int(input("enter a num between 1 and 6:"))
    if choice == 1:
        a = int(input("enter a  first number: "))
        b  = int(input("enter a  second number: "))
        print(module1.add(a,b))
    elif choice == 2:
        a = int(input("enter a first number: "))
        b = int(input("enter a  second number: "))
        print(module1.sub(a,b))
    elif choice == 3:
        a = int(input("enter a  first number: "))
        b = int(input("enter a  second number: "))
        print(module1.mul(a,b))
    elif choice == 4:
        a = int(input("enter a  first number: "))
        b = int(input("enter a  second number: "))
        print(module1.div(a,b))
    elif choice == 5:
        a = int(input("enter a  first number: "))
        b = int(input("enter a  second number: "))
        print(module3.power(a,b))
    elif choice == 6:
        a = int(input("enter a  number: "))
        print(module3.sqrt(a))
    elif choice == 7:
        print("EXIT")
        print("****** THANK YOU ******")
        
        
        
        

