import tkinter
import random
import time
from QnA import QnA


def startquiz(event):
    getquestion = questionBank.getquestion()
    introLabel.configure(text=getquestion[0])
    options(mainWindow, getquestion[1])
    startButton.destroy()


class options:
    buttons = []
    optionsFrame = 0

    def __init__(self, mainwindow, answers):
        self.optionsFrame = tkinter.LabelFrame(mainwindow, text='Choose a option')
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

    # def changeoptions(self, answers):
    #     self.optionsFrame.pack_forget()
    #     for i in range(0,4,1):
    #         self.buttons[i].grid_forget()
    #         self.buttons[i].configure(text=answers[i])
    #     order = random.sample(range(0, 4, 1), 4)
    #     for i in range(0, 4, 1):
    #         self.buttons[order.index(i)].grid(row=i)
    #     self.optionsFrame.pack()

    def correctoption(self, event):
        getquestion = questionBank.getquestion()
        introLabel.configure(text=getquestion[0])
        self.optionsFrame.pack_forget()
        for i in range(0,4,1):
            self.buttons[i].grid_forget()
            self.buttons[i].configure(text=getquestion[1][i])
        order = random.sample(range(0, 4, 1), 4)
        for i in range(0, 4, 1):
            self.buttons[order.index(i)].grid(row=i)
        self.optionsFrame.pack()
        return 1

    def wrongoption(self, event):
        getquestion = questionBank.getquestion()
        introLabel.configure(text=getquestion[0])
        self.optionsFrame.pack_forget()
        for i in range(0, 4, 1):
            self.buttons[i].grid_forget()
            self.buttons[i].configure(text=getquestion[1][i])
        order = random.sample(range(0, 4, 1), 4)
        for i in range(0, 4, 1):
            self.buttons[order.index(i)].grid(row=i)
        self.optionsFrame.pack()
        return 0


mainWindow = tkinter.Tk()
mainWindow.geometry('600x250+250+250')
mainWindow.resizable(False, False)
mainWindow.title('Q&J Quiz')
questionBank = QnA()
questionFrame = tkinter.LabelFrame(mainWindow, text='Correct Answers: 0/0')
introLabel = tkinter.Label(questionFrame, text='Welcome to this Quiz, Press Start!',
                           font=("Arial", 14), wraplength=550)
startButton = tkinter.Button(questionFrame, text='START')
questionFrame.pack()
introLabel.pack()
startButton.pack()
startButton.bind('<Button-1>', startquiz)
mainWindow.mainloop()