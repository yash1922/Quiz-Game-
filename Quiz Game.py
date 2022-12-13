print('''
 ___       __   _______   ___       ________  ________  _____ ______   _______      
|\  \     |\  \|\  ___ \ |\  \     |\   ____\|\   __  \|\   _ \  _   \|\  ___ \     
\ \  \    \ \  \ \   __/|\ \  \    \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|    
 \ \  \  __\ \  \ \  \_|/_\ \  \    \ \  \    \ \  \\\  \ \  \\|__| \  \ \  \_|/__  
  \ \  \|\__\_\  \ \  \_|\ \ \  \____\ \  \____\ \  \\\  \ \  \    \ \  \ \  \_|\ \ 
   \ \____________\ \_______\ \_______\ \_______\ \_______\ \__\    \ \__\ \_______|
    \|____________|\|_______|\|_______|\|_______|\|_______|\|__|     \|__|\|_______|
                                                                                 
''')
a=input("Enter your Name: ")
print(" Hello",a,"this is a quiz that will determine how much you know about Python")
print("The Rules are as follows:")
print("1. The questions are in True or False form.")
print("2. Make sure that you follow the case sensitivity as mentioned below:")
print(".\t Write \'True\' if The statement is correct.")
print(".\t Write \'False\' if The statement is incorrect.")
print("You will get 10 points for each right answer.")
print("There will be 5 questions in the quiz.")


def quiz():
    score=0
    questions= [
        {
            'question':"1.Python is a compiler language?",
            'answer':'False'
        },
        {
            'question': "2.Tim berners lee invented python?",
            "answer":"False"   
        },
        {
            'question': "3.Python was develpoed in 1991?",
            "answer":"True"
        },
        {
            'question':"4. 137000 libraries are there in python?",
            "answer":"True"
        },
        {
            'question':"5.Python is a case sensitive language?",
            "answer":"True"
        }
]
    for question in questions:

        question_text = question.get("question")
        print(question_text)

        user_answer= input("Enter answer: ")
        correct_answer= question.get("answer")

        if user_answer == correct_answer:
            score = score + 10
    print("Congratulations on completing the quiz")

    print("Your Score=",score)
    if score == 50:
        print("You have Aced the Quiz")
    else:
        print("Try hard next time.")


b=input("If you are ready type Yes if not type No: ")
if b == ("Yes"):
    print("Lets begin")
    quiz()
else:

    print("You have exited the quiz")



