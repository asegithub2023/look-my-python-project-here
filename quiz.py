quiz={
1:{
'question':'what is the capital city of Ethiopia?',
'answer':'Addis Ababa'
},

2:{
'question':'what is the capital city of America?',
'answer':'Washington D.C'
},

3:{
'question':'what is the capital city of China?',
'answer':'Beijing'
},

4:{
'question':'what is the capital city of canada?',
'answer':'ottawa'
},

5:{
'question':'what is the capital city of France?',
'answer':'Paris'
},

}




def run_quiz():
    score=0
    while True:
        for key,value in quiz.items():
            print(value['question'])
            user_answer=input("answer?: ")
            if user_answer.lower()==value['answer'].lower():
                score+=1
            else:
                print("Wrong,the answer is "+value['answer']+"\n")

        print(f"you got {score} out of 5 questions correctly")
        print("your percentage is "+str(int(score/5*100))+"%")

        choice=input("Do you want to take it again(Y/n)?")
        if choice=='y':
            run_quiz()
        else:
          print("Have a nice day")
          break
run_quiz()