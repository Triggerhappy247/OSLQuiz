import tkinter
from QnA import QnA


def startquiz(event):
    introLabel.configure(text=questionBank.getquestion()[0])
    startButton.destroy()

def choseoption(event):
    return 1

mainWindow = tkinter.Tk()
mainWindow.geometry('600x250+250+250')
mainWindow.resizable(False, False)
mainWindow.title('Q&J Quiz')
questionBank = QnA()
introLabel = tkinter.Label(mainWindow, text='Welcome to this Quiz, Press Start!',
                           font=("Arial", 14), wraplength=550)
startButton = tkinter.Button(mainWindow, text='START')
introLabel.pack()
startButton.pack()
startButton.bind('<Button-1>', startquiz)
mainWindow.mainloop()