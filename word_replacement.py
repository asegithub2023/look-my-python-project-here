
def replace_word():
    word_to_replace=input("enter the word to replace:  ")
    word_replacement=input("enter the word replacemet: ")

    
    words="Hi,I am Asefa Negash hi hi hi"
    # Replace the word in the string with the replacement word
    replaced_words=words.replace(word_to_replace,word_replacement)
    print(replaced_words)
    choice=input("Do you want to continue (y/n)?").lower()
    if choice=='y':
        replace_word()
    elif choice=='n':
        print("Have a nice day")
        exit()


replace_word()