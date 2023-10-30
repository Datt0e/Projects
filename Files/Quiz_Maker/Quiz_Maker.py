from random import randint

num_questions = int(input("Number of questions: "))

with open("Questions.txt", "r") as questions:
    contents = questions.readlines()
    length = len(contents)

    for i in range(num_questions): 
        #Get random questions of files num_questions times
        pass