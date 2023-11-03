import random
def roll_die():
    choice=input("Do you wanna roll(Y/N)? ")
    while choice.lower()=='Y'.lower():
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(f"dice rolled: {dice1} and {dice2}")
        choice=input("Do you wanna to roll again(Y/N)? ")

roll_die()
print("Have a nice day!")