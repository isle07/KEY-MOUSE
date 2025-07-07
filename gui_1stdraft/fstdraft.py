from tkinter import *
import pyautogui
import time
root = Tk()
root.title("KEY-MOUSE")
root.geometry("800x600")
root.resizable(False, False)

fstlabel = Label(root, text="행복한 오토 마우스^^")
fstlabel.pack()

fstentry = Entry(root, width=30)
fstentry.pack()
fstentry.pack_forget()

def sizak():
    fstlabel.config(text="반복할 횟수(자연수만)")
    startbtn.pack_forget()
    fstentry.pack_configure()
    continuebtn.pack_configure()


startbtn = Button(root, padx=30, pady=10, text='시작', command=sizak)
startbtn.pack()

Xentry = Entry(root, width=30)
Xentry.pack()
Xentry.pack_forget()
Yentry = Entry(root, width=30)
Yentry.pack()
Yentry.pack_forget()

def continuebtncmd2():
    global Xcon
    global Ycon
    Xcon = int(Xentry.get())
    Ycon = int(Yentry.get())
    Xentry.pack_forget()
    Yentry.pack_forget()
    fstlabel.config(text='정말 시작하시겠습니까?')
    continuebtn.config(command=continuebtncmd3)

def continuebtncmd3():
    for i in range(rptnum):
        pyautogui.moveTo(Xcon, Ycon)
        pyautogui.click()
        time.sleep(1)
        

    


def continuebtncmd():
    global rptnum
    rptnum = int(fstentry.get())
    #print(rptnum)
    fstlabel.config(text='위치 지정(위:x좌표, 아래:y좌표)(자연수만)')
    fstentry.pack_forget()
    Xentry.pack_configure()
    Yentry.pack_configure()
    continuebtn.pack_forget()
    continuebtn.pack_configure()
    continuebtn.config(command=continuebtncmd2)

continuebtn = Button(root, padx=20, pady=5, text='계속', command = continuebtncmd)
continuebtn.pack()
continuebtn.pack_forget()

root.mainloop()
