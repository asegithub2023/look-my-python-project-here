def get_input():
    num1=int(input("enter the first integer? "))
    num2 = int(input("enter the second integer? "))
    return num1,num2

def add():
    x,y=get_input()
    return x+y
def sub():
    x,y=get_input()
    return x- y
def mult():
    x, y = get_input()
    return x*y
def div():
    x, y = get_input()
    return x//y

def errorHandler():
    return "invalid choice"


print('''
Welcome to calculator
1.add
2.sub
3.mult
4.div
''')
choice=int(input("enter your choice? "))

operations={1:add,2:sub,3:mult,4:div}
output=operations.get(choice,errorHandler)()
print(output)