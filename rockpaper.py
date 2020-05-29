from tkinter import *
import random


def btn(click):
    global human
    human=str(click)
    inputvar.set(human)
    btn1()
    score()

def btn1():
    global cmptr
    cmptr = random.choices(['rock', 'paper', 'scissor'])
    cmptrvar.set(cmptr)

def score():
    global human_score
    global cmptr_score

    if cmptr==['rock'] and human=='paper':
      human_score=human_score+1
    elif cmptr==['paper'] and human=='scissor':
        human_score=(human_score)+1
    elif cmptr==['scissor'] and human=='rock':
        human_score=(human_score)+1
    elif cmptr==[human]:
        print('tie')
    else:
        cmptr_score=(cmptr_score)+1

    yourscr.set(human_score)
    cmptrscr.set(cmptr_score)


def end():
    exit()



win=Tk()
win.title("Rock Paper Scissors")
label=Label(win)
label.pack()
win.config(bg='black')

human=''
inputvar=StringVar()

cmptr=''
cmptrvar=StringVar()

human_score=0
yourscr=StringVar()

cmptr_score=0
cmptrscr=StringVar()

frame1=Frame(label,relief=SUNKEN,bg="gray15",bd=10)
frame1.pack(side=RIGHT,anchor=NW)

def result():
    print(cmptr_score)
    print(human_score)
    if cmptr_score>human_score:
      label=Label(frame1,text='You Lose',bg="gray15",fg='red',font=('arial',15,'bold')).grid(row=5,sticky=SW,column=3,columnspan=2)


    elif cmptr_score<human_score:
        label1=Label(frame1,text='You Win',bg="gray15",fg='green',font=('arial',15,'bold')).grid(row=5,sticky=SW,column=3,columnspan=2)
    else:
        label1 = Label(frame1, text='Game is Tie',bg="gray15", fg='green', font=('arial', 15, 'bold')).grid(row=5,sticky=SW,column=3,columnspan=2)

#GUI Programming
labelhuman=Label(frame1,text='You:',font=('arial',15,'bold'),fg='green',bg="gray15").grid(row=1,sticky=E,column=2)
labelcmptr=Label(frame1,text='Computer:',font=('arial',15,'bold'),fg='red',bg="gray15").grid(row=2,sticky=E,column=2)

humanentry=Entry(frame1,bg='black',fg='white',font=('arial',15,'bold'),textvariable=inputvar,relief=SUNKEN,bd=15).grid(row=1,column=3)
cmptrentry=Entry(frame1,bg='black',fg='white',font=('arial',15,'bold'),textvariable=cmptrvar,relief=SUNKEN,bd=15).grid(row=2,column=3)

buttonrock=Button(frame1,text='Rock',bd=5,fg='white',bg='black',relief=SUNKEN,padx=16,pady=16,command=lambda:btn('rock'),font=('arial',15,'bold')).grid(row=1,sticky=W,column=1)
buttonpaper=Button(frame1,text='Paper',bd=5,fg='white',bg='black',relief=SUNKEN,padx=13,pady=10,command=lambda:btn('paper'),font=('arial',15,'bold')).grid(row=2,sticky=W,column=1)
buttonscissor=Button(frame1,text='scissor',bd=5,fg='white',bg='black',relief=SUNKEN,padx=11,pady=10,command=lambda:btn('scissor'),font=('arial',15,'bold')).grid(row=3,sticky=W,column=1)

humanscore=Label(frame1,text='Your Score:',font=('arial',15,'bold'),fg='green',bg="gray15").grid(column=2,row=3,sticky=E)
cmptrscore=Label(frame1,text='Computer Score:',font=('arial',15,'bold'),fg='red',bg="gray15").grid(column=2,row=4,sticky=E)

hmn_scr_entry=Entry(frame1,bg='black',fg='green',font=('arial',15,'bold'),textvariable=yourscr,relief=SUNKEN,bd=15).grid(row=3,column=3)
cmptr_scr_entry=Entry(frame1,bg='black',fg='red',font=('arial',15,'bold'),textvariable=cmptrscr,relief=SUNKEN,bd=15).grid(row=4,column=3)

btn_end=Button(frame1,text='End',bd=5,fg='white',bg='black',relief=SUNKEN,padx=16,pady=16,command=end,font=('arial',15,'bold')).grid(row=5,column=1,sticky=W)

result=Button(frame1,text='Result',command=result,bd=5,fg='white',bg='green',relief=SUNKEN,padx=16,pady=16,font=('arial',15,'bold')).grid(row=4,column=1,sticky=W)

win.mainloop()