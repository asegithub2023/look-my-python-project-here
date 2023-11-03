alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
          'p','q','r','s','t','u','v','w','x','y','z']

try:
    def encryption(plain_text,shift_key):
        cipher_text=" "
        for char in plain_text:
            if char in alphabet:
                position=alphabet.index(char)
                new_position=(position+shift_key)%26
                cipher_text+=alphabet[new_position]
            else:
                cipher_text+=char#put any number or special symbol as it is
        print(f"Here's the text after encryption: {cipher_text}")
    

    def decryption(cipher_text,shift_key):
        plain_text=" "
        for char in cipher_text:
            if char in alphabet:
                position=alphabet.index(char)
                new_position=(position-shift_key)%26
                plain_text+=alphabet[new_position]
            else:
                plain_text+=char

        print(f"Here's the text after decryption: {plain_text}")


    want_end=False#I don't want to end now
    while not want_end:
        choice=int(input("Type 1 for encryption,2 type for decryption:  "))
        words=input("Type your message:  ")
        words=words.lower()
        key=int(input("Type shift number:  "))

        if choice==1:
            encryption(words,key)
        elif choice==2:
            decryption(words,key)
        cont=input("Do you want to continue(y/n)? ")
        if cont=='n':
            wan_end=True
            print("Have a nice day")
except(ValueError):
    print("invalid input")




