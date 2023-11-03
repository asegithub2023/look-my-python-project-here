import random
import string
def password_generator():
    print()
    print("Welcome to the password generator!")
    try:

        num_letters=int(input("how many letters would you like in your password? "))
        password=""
        for _ in range(0,num_letters):
            password+=random.choice(string.ascii_letters)


        num_symbols=int(input("how many symbols would you like in your password? "))
        symbols="!@#$%^&*()_+|{}[]:,';.~`<>?/"
        for _ in range(0,num_symbols):
            password+=random.choice(symbols)


        num_numbers=int(input("how many numbers would you like in your password?"))
        for _ in range(0,num_numbers):
            password+=str(random.randint(0,9))

        print()
        print("your easy password is:",password)

        #changing password to list
        change_tolist=list(password)
        #shuffling list
        random.shuffle(change_tolist)
        #changing shuffled list to string
        mixed_password=''.join(change_tolist)
        print(f"your shuffle password is:  {mixed_password}\n")
        choice=input("Do you want to generate other password(y/n)?").lower()
        if choice=="y":
            password_generator()
        elif choice=="n":
            print("Have a nice day")
            exit()
        else:
            print("incorrect choice")
    except (ValueError):
        print("invalid input")

password_generator()
