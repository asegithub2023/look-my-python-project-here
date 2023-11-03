import random

EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5

def set_difficulty(level):
    if level=='easy':
        return EASY_LEVEL_ATTEMPTS
    if level=='hard':
       return HARD_LEVEL_ATTEMPTS


def check_answer(guessed_number,answer,attemts):
    if guessed_number<answer:
        print("your guess is too low")
        return attemts- 1
    elif guessed_number>answer:
        print("your guess is to high")
        attemts=attemts- 1
        return attemts
    else:
        print(f"your guess is right...The answer was {answer}")



def game():
    print("Let me thing of a number between 1 to 100 ")
    answer=random.randint(1,100)
    print(answer)
    level=input("choose level of dificulty Type 'easy' or 'hard:  ")
    attemts=set_difficulty(level)

    guessed_number=0
    while guessed_number!=answer:
        print(f"you have {attemts} reamining to guess the number")

        guessed_number=int(input("Guess number "))
        attemts=check_answer(guessed_number,answer,attemts)
        if attemts==0:
            print("you are out of guess...you loose")
            return
        elif guessed_number!=answer:
            print("guess again")
game()




