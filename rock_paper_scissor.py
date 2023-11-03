"""
This program asks user to inter his/her choice i.e 1 for rock 2 for paper and 3 for 
scissors computer will generate a random number from 0 to 2 using random function
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
Both players choose the same option it is tie the game is played again
0 for Rock
1 for Paper
2 for Scissors

"""


import random
computer_choice=random.randint(0,2)
print(computer_choice)

user_choice=int(input("enter your choice(0 for Rock,1 for Paper,2 for Scissors)? "))
if user_choice<0 or user_choice>2:
    print("you entered wrong option and you loose")
    exit()
list=[0,1,2]
choice={"rock":0,"Paper":1,"Scissors":2}
computer_choice=random.choice(list)
print(f"computer choice is {computer_choice}")
if user_choice==0 and computer_choice==2:
        print("you win")
elif user_choice==2 and computer_choice==0:
        print("you loose")
elif user_choice>computer_choice:
        print("you win")
elif user_choice<computer_choice:
        print("you loose")
else:
        print("it's a draw, please try again later")
