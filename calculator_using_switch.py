def get_input():
    num1=int(input("enter the first integer? "))
    num2 = int(input("enter the second integer? "))
    return num1,num2

def add():
    x,y=get_input()
    print(x+y)
def sub():
    x,y=get_input()
    print(x - y)
def mult():
    x, y = get_input()
    print(x * y)
def div():
    x, y = get_input()
    print(x // y)

def errorHandler():
    print("invalid choice")


print('''
Welcome to calculator
1.add
2.sub
3.mult
4.div
''')
choice=int(input("enter your choice? "))
match choice:
    case 1:
        add()
    case 2:
        sub()
    case 3:
        mult()
    case 4:
        div()

    case default:
        errorHandler()

