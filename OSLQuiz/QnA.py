import linecache


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


test = QnA()
print(test.qmax)
