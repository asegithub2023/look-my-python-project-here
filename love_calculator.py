print()
print("WELCOME TO TRUE CALCULATOR\n")
name1=input("enter your full name? \n")
name2=input("enter your friend full name? \n")
names=name1+name2

names_small=names.lower()

#TRUE LOVE
while True:
    true=names_small.count('t')+names_small.count('r')+names_small.count('u')+names_small.count('e')
    love=names_small.count('l')+names_small.count('o')+names_small.count('v')+names_small.count('e')

    Love_score=int(str(true)+str(love))

    if Love_score<10 and Love_score>90:
        print(f"your love is score {Love_score} and you can talk right now")
    elif Love_score>=40 and Love_score<=50:
        print(f"your love score is {Love_score} and you are already familiar ")
    else:
        print(f"your love score is  {Love_score}")
    choice=input("Dou you want to continue?(y/n)\n").lower()
    if choice=='y':
        name1=input("enter your full name? \n")
        name2=input("enter your friend full name? \n")
        names=name1+name2
        names_small=names.lower()
    else:
        print("Have a nice day")
        break