from random import randint

quiz_contents = []
random_num = []
num_questions = int(input("Number of questions: "))

with open("Questions.txt", "r") as questions:
    contents = questions.readlines()
    length = len(contents)

    for i in range(num_questions): 
        while True:    
            chosen_ques = randint(0,length - 1)
            if chosen_ques in random_num:
                continue
            else:
                break
        random_num.append(chosen_ques)
        quiz_contents.append(contents[chosen_ques])

with open("Quiz.txt","w") as quiz:  
    for question in quiz_contents:
        quiz.write(question)

