import random
capitals = {'广东省': '广州','湖南省': '长沙','四川省': '成都','湖北省': '武汉','云南省': '昆明'}
for quizNum in range(3):                                                            #创建3份试题
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1),'w')                       #创建测试题文件
    answerFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1),'w')             #创建答案文件
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20)+'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    states = list(capitals.keys())                                                  #建立省份列表
    random.shuffle(states)                                                          #用shuffle()函数打乱
    for questionNum in range(5):                                                    #创建5道习题
        correctAnswer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]                           #删除正确答案
        wrongAnswer = random.sample(wrongAnswer,3)                                  #创建错误答案
        answerOption = wrongAnswer + [correctAnswer]                                #建立答案选项
        random.shuffle(answerOption)
        quizFile.write('%s.What is the capital of %s?\n' % (questionNum +1,states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i] ,answerOption[i]))
        quizFile.write('\n')
        answerFile.write('%s. %s\n' % (questionNum + 1,'ABCD'[answerOption.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()