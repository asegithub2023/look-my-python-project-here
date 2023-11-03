def word_dict():
    dict={

        'database':'Its a collection of related data',
        'computer':'electronic device which takes input and produce desired output',

        'information':'collection of fats and figures that have a meaning'
    }

    while True:
        user_input=input("input word? ").lower()
        
        # Check if the user input exists in the dictionary
        if user_input in dict:
            print(user_input,":",dict[user_input]) 
            choice=input("Do you want to quit(y/n)?")
            if choice=='y':
                print("Have a nice day")
                break

        elif user_input not in dict:
            print("word you are looking is not found")
            break
          
   
word_dict()


     
