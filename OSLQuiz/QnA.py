import linecache
import random


class QnA:
    qmax = 0

    @staticmethod
    def filelen(fname):
        with open(fname, encoding="utf8") as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def __init__(self):
        self.qmax = QnA.filelen('../QnA/questions.txt')

    def getquestion(self):
        qnumber = random.randrange(0, self.qmax, 1)
        question = linecache.getline('../QnA/questions.txt', qnumber)[:-1]
        answers = linecache.getline('../QnA/answers.txt', qnumber)[:-1].split(',')
        return question, answers


test = QnA()
print(test.qmax)
question = test.getquestion()
print(question[0])
print(question[1])

