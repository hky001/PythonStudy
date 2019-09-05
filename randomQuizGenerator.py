import random
capitals = {'广东省': '广州','湖南省': '长沙','四川省': '成都','湖北省': '武汉','云南省': '昆明'}
for quizNum in range(3):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1),'w')
    answerFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1),'w')
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20)+'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(5):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer,3)
        answerOption = wrongAnswer + [correctAnswer]
        random.shuffle(answerOption)
        quizFile.write('%s.What is the capital of %s?\n' % (questionNum +1,states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i] ,answerOption[i]))
        quizFile.write('\n')
        answerFile.write('%s. %s\n' % (questionNum + 1,'ABCD'[answerOption.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()