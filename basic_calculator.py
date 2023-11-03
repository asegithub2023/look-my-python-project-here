def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
     return a*b

def div(a,b):
    return a/b


while True:
        try:
            print("WELCOME TO BASIC CALCULATOR\n")
            print("Type 1 for add, 2 for sub 3 for mult and 4 for div, 5 for quit")
            choice=int(input("enter you choice:? "))
            
            if choice==1:
                num1=int(input("enter the first number:? "))
                num2=int(input("enter the second number:? "))
                result=add(num1,num2)
                print(str(num1)+ "+"+str(num2)+" ="+str(result)+"\n")

            elif choice==2:
                num1=int(input("enter the first number:? "))
                num2=int(input("enter the second number:? "))
                result=sub(num1,num2)
                print(str(num1)+ "-"+str(num2)+"="+str(result))

            elif choice==3:
                num1=int(input("enter the first number:? "))
                num2=int(input("enter the second number:? "))
                result= mult(num1,num2)
                print(str(num1)+ "*"+str(num2)+"="+str(result))

            elif choice==4:
                num1=int(input("enter the first number:? "))
                num2=int(input("enter the second number:? "))
                result=div(num1,num2)
                print(str(num1)+ "/"+str(num2)+"="+str(result))

            elif choice==5:
                print("program is ended!")
                quit()
            else:
                print("invlaid choice")
    
        except(ZeroDivisionError):
            print("you can't divide by zer")
        except(ValueError):
            print("invalid input")