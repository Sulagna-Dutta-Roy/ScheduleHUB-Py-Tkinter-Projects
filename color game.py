import tkinter
import random

colours = ['Red', 'Blue', 'Purple', 'Black', 'Yellow', 'orange']
score = 0

timeleft = 30

def startgame(event):
    if timeleft == 30:
       countdown()

    nextcolour()

def nextcolour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1

        e.delete(0, tkinter.END)
        random.shuffle(colours)

        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score" + str(score))

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1

        timeLabel.config(text="Time left"+ str(timeleft))
        timeLabel.after(1000,countdown)


root = tkinter.Tk()
root.title("Color Game")
root.geometry("375x260")

instructions = tkinter.Label(root, text="Type in the colour of the words,and not in the text!", font=('Helvetica',12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="press enter to start", font=('Helvetica',12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time Left"+str(timeleft), font=('Helvetica',12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica',60))
label.pack()

e = tkinter.Entry(root)

root.bind('<Return>', startgame)
e.pack()
e.focus_set()
root.mainloop()












