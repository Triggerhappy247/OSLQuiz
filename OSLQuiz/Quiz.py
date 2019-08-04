import tkinter
import random
from QnA import QnA


def startquiz(event):
    getquestion = questionBank.getquestion()
    introLabel.configure(text=getquestion[0])
    options(mainWindow, getquestion[1])
    startButton.destroy()


class options:
    buttons = []
    optionsFrame = 0
    answerFrame = 0
    nextButton = 0
    answerLabel = 0

    def __init__(self, mainwindow, answers):
        self.optionsFrame = tkinter.LabelFrame(mainwindow, text='Choose a option')
        self.answerFrame = tkinter.LabelFrame(mainwindow, text='Correct Answer was:')
        self.answerLabel = tkinter.Label(self.answerFrame, text=answers[0],
                           font=("Arial", 14), wraplength=550)
        self.nextButton = tkinter.Button(self.answerFrame, text='Next Question')
        self.nextButton.bind('<Button-1>', self.nextquestion)
        self.answerLabel.pack()
        self.nextButton.pack()
        for i in range(0, 4, 1):
            self.buttons.append(tkinter.Button(self.optionsFrame, text=answers[i], activebackground='light gray'))
            if i == 0:
                self.buttons[0].bind('<Button-1>', self.correctoption)

            else:
                self.buttons[i].bind('<Button-1>', self.wrongoption)
        order = random.sample(range(0,4,1),4)
        for i in range(0,4,1):
            self.buttons[order.index(i)].grid(row=i)
        self.optionsFrame.pack()

    def correctoption(self, event):
        global questionFrame
        global correct
        global total
        correct += 1
        total += 1
        questionFrame.configure(text='Correct Answers: '+ str(correct) + '/'+ str(total))
        self.answerFrame.configure(text='You\'re Absolutely Right!')
        self.optionsFrame.pack_forget()
        self.answerFrame.pack()
        return 1

    def wrongoption(self, event):
        global questionFrame
        global total
        total += 1
        questionFrame.configure(text='Correct Answers: ' + str(correct) + '/' + str(total))
        self.answerFrame.configure(text='Wrong! Correct Answer was:')
        self.optionsFrame.pack_forget()
        self.answerFrame.pack()
        return 0

    def nextquestion(self, event):
        getquestion = questionBank.getquestion()
        introLabel.configure(text=getquestion[0])
        self.answerLabel.configure(text=getquestion[1][0])
        for i in range(0, 4, 1):
            self.buttons[i].grid_forget()
            self.buttons[i].configure(text=getquestion[1][i])
        order = random.sample(range(0, 4, 1), 4)
        for i in range(0, 4, 1):
            self.buttons[order.index(i)].grid(row=i)
        self.answerFrame.pack_forget()
        self.optionsFrame.pack()
        return 1




mainWindow = tkinter.Tk()
mainWindow.geometry('600x300+250+250')
mainWindow.resizable(False, False)
mainWindow.title('Q&J Quiz')
questionBank = QnA()
total = 0
correct = 0
questionFrame = tkinter.LabelFrame(mainWindow, text='Correct Answers: '+ str(correct) + '/'+ str(total))
introLabel = tkinter.Label(questionFrame, text='Welcome to this Quiz, Press Start!',
                           font=("Arial", 14), wraplength=550)
startButton = tkinter.Button(questionFrame, text='START')
questionFrame.pack()
introLabel.pack()
startButton.pack()
startButton.bind('<Button-1>', startquiz)
mainWindow.mainloop()
