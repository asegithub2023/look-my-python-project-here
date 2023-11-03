def get_input():
    num1=int(input("enter the first integer? "))
    num2 = int(input("enter the first integer? "))
    return num1,num2

def add():
    x,y=get_input()
    return x+y
def sub():
    x,y=get_input()
    return x - y
def mult():
    x, y = get_input()
    return x * y
def div():
    x, y = get_input()
    return x // y

print('''
Welcome to calculator
1.add
2.sub
3.mult
4.div
''')
choice=int(input("enter your choice? "))
operations=[add,sub,mult,div]
if choice>len(operations):
    print("list index of range please try again")
else:
    result=operations[choice-1]()      #if choice=1 this line is the same as add()
    print(result)
