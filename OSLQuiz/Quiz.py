import tkinter

mainWindow = tkinter.Tk()
mainWindow.geometry('500x500+250+250')
mainWindow.title('Q&J Quiz')
introLabel = tkinter.Label(mainWindow,text='Welcome to this Quiz, Press Start!')
startButton = tkinter.Button(mainWindow,text='START')
introLabel.pack()
startButton.pack()
mainWindow.mainloop()